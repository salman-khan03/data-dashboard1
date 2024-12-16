import taipy as tp
import taipy.gui.builder as tgb
from taipy.gui import Icon
from taipy import Config

# create page
with tgb.Page() as page:
    tgb.text("my beautiful application goes here!")

if __name__ == "__main__":
    gui = tp.Gui(page)
    gui.run(title = "Data Sceince Dashboard")
