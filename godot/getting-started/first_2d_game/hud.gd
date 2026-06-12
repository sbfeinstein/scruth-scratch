extends CanvasLayer

signal start_game

func _on_start_button_pressed() -> void:
	$StartButton.hide()
	start_game.emit()

func _on_message_timer_timeout() -> void:
	$Message.hide()

func show_game_over():
	show_message_briefly("Game Over")
	await $MessageTimer.timeout
	
	$Message.text = "Dodge the Creeps (Again)!"
	$Message.show()
	
	# Dynamic one-shot timer after game ends and before we show the Start button again
	await get_tree().create_timer(1.0).timeout
	
	$StartButton.show()

func show_message_briefly(text: StringName) -> void:
	$Message.text = text
	$Message.show()
	$MessageTimer.start()

func update_score(score: int) -> void:
	$ScoreLabel.text = str(score)
