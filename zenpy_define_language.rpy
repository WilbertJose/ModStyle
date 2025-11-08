init python:
   config.language = "es_zenpy"
   config.default_language = "es_zenpy"
   config.rollback_enabled = True

screen quick_menu():

   zorder 100

   if quick_menu:

      hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Volver") action Rollback()
            textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Ajustes") action ShowMenu('preferences')