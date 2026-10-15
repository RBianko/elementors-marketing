extends SceneTree

var _frames := 0

func _process(_delta: float) -> bool:
	_frames += 1
	# Autoloads load balance data on their first frames.
	if _frames < 3:
		return false
	_scan()
	return true

func _env(key: String, fallback: int) -> int:
	var v := OS.get_environment(key)
	return int(v) if v.is_valid_int() else fallback

func _scan() -> void:
	var rs = root.get_node("RunState")
	var bal = root.get_node("Balance")
	var sb = root.get_node("SignalBus")
	var harness = load("res://tests/shot_movie.gd").new()
	var target_round := _env("SCAN_ROUND", 3)
	var target_level := _env("SCAN_LEVEL", 3)
	var rerolls := _env("SCAN_REROLLS", 3)
	for s in range(_env("SCAN_FROM", 1), _env("SCAN_TO", 200) + 1):
		seed(s)
		rs.reset(0)
		rs.master_seed = s
		rs.dice = harness._build_dice(["fire", "ice", "wind"])
		sb.run_started.emit()
		while rs.round < target_round:
			if not rs.advance_round():
				break
		while rs.player_level < target_level:
			if not rs.grant_xp(bal.xp_curve(rs.player_level)):
				break
		var line := "SEED %d | s0 %s" % [s, _shop(rs)]
		for k in rerolls:
			rs.shop_refresh_idx += 1
			rs._reroll_visible_slots()
			line += " | r%d %s" % [k + 1, _shop(rs)]
		print(line)

func _shop(rs) -> String:
	var out: PackedStringArray = []
	for i in rs.shop.size():
		var u = rs.shop[i]
		out.append("-" if u == null else "%s/%s/%d%s" % [u.type_id, u.element_id, u.star, ("*" + String(u.offer_kind)) if u.offer_kind != &"" else ""])
	return " ".join(out)
