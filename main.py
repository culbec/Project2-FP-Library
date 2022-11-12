from tests.tests import Tester
from ui.ui import UI

tester = Tester()
ui = UI()

tester.run_all_tests()
ui.run_ui()

