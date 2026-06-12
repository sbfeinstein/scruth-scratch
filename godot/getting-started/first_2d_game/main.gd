extends Node

@export var mob_scene: PackedScene
var score: int

func _ready() -> void:
	window_size(480, 720)
	$Player.hide()
	update_score(0)

func window_size(width: int, height: int) -> void:
	var window := get_window()
	window.content_scale_mode = Window.CONTENT_SCALE_MODE_CANVAS_ITEMS
	window.content_scale_aspect = Window.CONTENT_SCALE_ASPECT_KEEP
	window.content_scale_size = Vector2i(width, height)
	window.size = Vector2i(width*2, height*2)
	DisplayServer.window_set_size(Vector2i(width*2, height*2))

func new_game() -> void:
	get_tree().call_group("mobs", "queue_free")
	update_score(0)
	$HUD.show_message_briefly("Get Ready")
	
	$Player.start($StartPosition.position)
	$Player.show()
	$Music.play()
	$StartTimer.start()

func _on_start_timer_timeout() -> void:
	$MobTimer.start()
	$ScoreTimer.start()

func _on_mob_timer_timeout() -> void:
	var spawn_location: PathFollow2D = $MobPath/MobSpawnLocation
	spawn_location.progress_ratio = randf() # random float will be between 0 and 1
	
	var direction = spawn_location.rotation + PI / 2 # have enemy face perpendicular to the path, inward (path is clockwise)
	direction += randf_range(-PI / 4, PI / 4) # A little direction randomness to be more interesting, plus or minus 45 degrees
	
	var velocity = Vector2(randf_range(150.0,250.0), 0) # Some randomness in speed for the cool factor.  Just horizontal vector since we set direction below.
	
	var new_mob: RigidBody2D = mob_scene.instantiate()
	new_mob.position = spawn_location.position
	new_mob.rotation = direction
	new_mob.linear_velocity = velocity.rotated(direction)
	
	add_child(new_mob)

func _on_score_timer_timeout() -> void:
	update_score(score + 1)

func update_score(new_score: int) -> void:
	score = new_score
	$HUD.update_score(score)

func game_over() -> void:
	$ScoreTimer.stop()
	$MobTimer.stop()
	
	$Music.stop()
	$DeathSound.play()
	
	$HUD.show_game_over()
