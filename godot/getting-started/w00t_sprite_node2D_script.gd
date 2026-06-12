extends "res://w00t_sprite_base_script.gd"

func _ready() -> void:
	var timer: Timer = get_node("VisibilityTimer")
	timer.timeout.connect(_on_visibility_timer_timeout)

func _on_button_pressed() -> void:
	set_process(not is_processing())

func _process(delta):
	rotation += angular_speed * delta
	var velocity = Vector2.UP.rotated(rotation) * speed
	position += velocity * delta

func _on_visibility_timer_timeout() -> void:
	visible = not visible
