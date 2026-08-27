# =========================================================
# notepad.rpy — persistent notepad, no story content
# =========================================================

default persistent.case_notes = ""

screen notepad_icon():
    zorder 200

    frame:
        xalign 1.0 yalign 0.0
        xoffset -20 yoffset 20
        background "#000000cc"
        padding (10, 10)

        button:
            action Show("notepad_screen")

            hbox:
                spacing 8
                add Solid("#f4f1e8", xsize=28, ysize=28)
                text "Notes" color "#ffffff" size 14 yalign 0.5

init python:
    config.overlay_screens.append("notepad_icon")


screen notepad_screen():
    modal True
    zorder 300

    default notes_draft = persistent.case_notes or ""

    add "#000000cc"

    frame:
        xalign 0.5 yalign 0.5
        xsize 600 ysize 400
        background "#1c1c1a"
        padding (20, 20)

        vbox:
            spacing 12

            text "Case Notes" size 22 color "#ffffff"

            frame:
                background "#f4f1e8"
                xsize 560 ysize 260
                padding (10, 10)

                input:
                    value ScreenVariableInputValue("notes_draft")
                    length 1000
                    color "#111111"
                    multiline True

            hbox:
                spacing 10
                xalign 1.0

                textbutton "Save":
                    action [
                        SetVariable("persistent.case_notes", notes_draft),
                        Hide("notepad_screen")
                    ]

                textbutton "Close":
                    action Hide("notepad_screen")