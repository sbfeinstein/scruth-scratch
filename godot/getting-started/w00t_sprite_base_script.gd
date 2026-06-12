extends Sprite2D

var speed=400
var angular_speed = PI

func _init() -> void:
	print("Yo, world!")

func _process(delta: float) -> void:
	var direction = 0
	if Input.is_action_pressed("ui_left"):
		direction = -1
	if Input.is_action_pressed("ui_right"):
		direction = 1

	# rotation += angular_speed * direction * delta
	rotation = fposmod(rotation + (angular_speed * direction * delta), TAU)
	
	var velocity = Vector2.ZERO
	if Input.is_action_pressed("ui_up"):
		velocity = Vector2.UP.rotated(rotation) * speed

	position += velocity * delta

# Kept as an example even if not calling in the _process loop
func autoMoveAndRotate(delta: float) -> void:
	# Keep rotation within 0 to 2*PI (which is TAU)
	# rotation += angular_speed * delta
	rotation = fposmod(rotation + angular_speed * delta, TAU)
	
	var velocity = Vector2.UP.rotated(rotation) * speed
	position += velocity * delta
