extends Button

var button_type = null

func _on_pressed() -> void:
	get_tree().change_scene_to_file("res://Scenes/Menus/introduction.tscn")
