import sys
import os
import re
import winsound
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QGraphicsDropShadowEffect,
    QMenu, QLineEdit, QDialog, QSlider, QPushButton, QHBoxLayout, QColorDialog
)
from PySide6.QtGui import QFont, QPainterPath, QRegion, QPainter, QColor, QBrush, QAction, QKeySequence
from PySide6.QtCore import QTimer, QRectF, Qt, QPoint, Signal, QSettings, QRect


ORGANIZATION_NAME = "YourCompanyName"
APPLICATION_NAME = "CountdownTimer"

class OpacitySliderWindow(QDialog):
    # ... (OpacitySliderWindow class remains IDENTICAL to the previous version) ...
    windowOpacityChanged = Signal(int)
    backgroundOpacityChanged = Signal(int)

    def __init__(self, parent=None, initial_window_opacity=100, initial_background_opacity=100):
        super().__init__(parent)
        self.setWindowTitle("Set Opacity")
        self.setWindowFlags(Qt.WindowType.Tool | Qt.WindowType.WindowStaysOnTopHint)

        self.window_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.window_slider.setRange(10, 100)
        self.window_slider.setValue(initial_window_opacity)
        self.window_slider.valueChanged.connect(self.windowOpacityChanged.emit)

        self.background_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.background_slider.setRange(0, 100)
        self.background_slider.setValue(initial_background_opacity)
        self.background_slider.valueChanged.connect(self.backgroundOpacityChanged.emit)

        self.window_label = QLabel("Window Opacity:", self)
        self.background_label = QLabel("Background Opacity:", self)

        layout = QVBoxLayout(self)
        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(self.window_label)
        h_layout1.addWidget(self.window_slider)
        layout.addLayout(h_layout1)
        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(self.background_label)
        h_layout2.addWidget(self.background_slider)
        layout.addLayout(h_layout2)
        self.setLayout(layout)
        self.adjustSize()

        if parent:
            parent_rect = parent.geometry()
            screen_rect = parent.screen().availableGeometry() if parent.screen() else QApplication.primaryScreen().availableGeometry()
            x = parent_rect.right() + 10
            y = parent_rect.top()
            if x + self.width() > screen_rect.right():
                x = parent_rect.left() - self.width() - 10
            if y + self.height() > screen_rect.bottom():
                y = screen_rect.bottom() - self.height() - 10
            self.move(max(screen_rect.left(), x), max(screen_rect.top(), y))

        self.parent_window = parent

    def closeEvent(self, event):
        if self.parent_window:
            self.parent_window.opacity_slider_window = None
        super().closeEvent(event)


class CountdownTimer(QMainWindow):
    def __init__(self, initial_secs_from_arg=None):
        super().__init__()

        self.settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        self.started_without_args = initial_secs_from_arg == 0

        saved_seconds = self.settings.value("initial_seconds", 0, type=int)
        if initial_secs_from_arg is not None:
            self.initial_seconds = initial_secs_from_arg
            print(f"Using time from command line argument: {self.initial_seconds}s")
        else:
            self.initial_seconds = saved_seconds
            print(f"Using time from settings: {self.initial_seconds}s")

        loaded_window_opacity_float = self.settings.value("window_opacity", 1.0, type=float)
        loaded_background_alpha = self.settings.value("background_alpha", 255, type=int)
        loaded_font_color_name = self.settings.value("font_color", "#FF0000", type=str)

        self.setWindowTitle('Countdown Timer')
        # --- MODIFICATION START ---
        # Define the REQUIRED initial geometry (including 0,0 position)
        self.initial_geometry = QRect(0, 0, 220, 100)
        # ALWAYS set the geometry to this initial state on startup
        self.setGeometry(self.initial_geometry)
        # Store this as the geometry to restore to when shrinking
        # This will be updated if the user moves the window while small
        self.original_geometry = self.geometry()
        # REMOVED: Loading saved geometry and centering logic
        # --- MODIFICATION END ---

        self.setStyleSheet("border-radius: 15px;")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.background_alpha = loaded_background_alpha
        self.font_color = QColor(loaded_font_color_name)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QColor(0, 0, 0, 180))
        self.shadow.setOffset(0, 0)

        self.container = QWidget()
        self.container.setGraphicsEffect(self.shadow)
        self.update_container_style()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.countdown)

        self.clockTime = QLabel(self)
        self.clockTime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.clockTime.setFont(QFont('Sophia Pro Soft', 60))
        self.update_font_color_style()

        self.time_input_box = QLineEdit(self)
        self.time_input_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_input_box.setFont(QFont('Sophia Pro Soft', 50))
        self.time_input_box.setStyleSheet("""
            color: white;
            background-color: rgba(51, 51, 51, 0.9);
            border: 1px solid red;
            border-radius: 5px;
            padding: 5px;
        """)
        self.time_input_box.setVisible(False)
        self.time_input_box.returnPressed.connect(self.handle_time_input)
        self.time_input_box.installEventFilter(self)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.clockTime)
        self.layout.addWidget(self.time_input_box)
        self.layout.setContentsMargins(10, 10, 10, 10)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.setWindowOpacity(loaded_window_opacity_float)

        self.time_left = self.initial_seconds
        self.paused = False
        self.timer_running = True
        self.is_enlarged = False
        # self.original_geometry is set above
        self.dragPos = None
        self.is_time_up = False
        self.is_input_mode = False
        self.opacity_slider_window = None

        self.setup_actions()

        if self.time_left > 0:
            self.timer.start(1000)
        else:
            self.timer_running = False
        self.update_display()

    # REMOVED the center_on_primary_screen method as it's no longer used in init

    def setup_actions(self):
        # ... (setup_actions remains IDENTICAL) ...
        self.pause_action = QAction("Pause Timer", self)
        self.pause_action.setShortcut(QKeySequence("Shift+Space"))
        self.pause_action.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.pause_action.triggered.connect(self.toggle_pause)
        self.addAction(self.pause_action)

        self.reset_action = QAction("Reset Timer", self)
        self.reset_action.setShortcut(QKeySequence("Shift+R"))
        self.reset_action.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.reset_action.triggered.connect(self.reset_timer)
        self.addAction(self.reset_action)

        self.close_action = QAction("Close Timer (`/~)", self)
        self.close_action.setShortcut(QKeySequence("`"))
        self.close_action.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.close_action.triggered.connect(self.close_app)
        self.addAction(self.close_action)

        self.change_time_action = QAction("Change Time...", self)
        self.change_time_action.triggered.connect(self.switch_to_input_mode)

        self.change_opacity_action = QAction("Change Opacity...", self)
        self.change_opacity_action.triggered.connect(self.open_opacity_sliders)

        self.change_font_color_action = QAction("Change Font Colour...", self)
        self.change_font_color_action.triggered.connect(self.change_font_color)

        self.save_settings_action = QAction("Save Settings", self)
        self.save_settings_action.triggered.connect(self.save_settings)


    def update_container_style(self):
        # ... (remains IDENTICAL) ...
        style = f"""
            background-color: rgba(0, 0, 0, {self.background_alpha});
            border-radius: 15px;
        """
        self.container.setStyleSheet(style)


    def update_font_color_style(self):
        # ... (remains IDENTICAL) ...
         style = f"""
             color: {self.font_color.name()};
             background-color: transparent;
         """
         self.clockTime.setStyleSheet(style)


    def set_background_opacity(self, value):
        # ... (remains IDENTICAL) ...
        self.background_alpha = int(value * 2.55)
        self.update_container_style()


    def set_window_opacity(self, value):
        # ... (remains IDENTICAL) ...
        opacity = value / 100.0
        super().setWindowOpacity(opacity)


    def paintEvent(self, event):
        # ... (remains IDENTICAL) ...
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.setPen(Qt.PenStyle.NoPen)
        rect = self.rect()
        radius = 15
        path = QPainterPath()
        path.addRoundedRect(QRectF(rect), radius, radius)
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)


    def update_display(self):
        # ... (remains IDENTICAL) ...
        if self.is_input_mode:
             return

        if self.is_time_up:
            self.clockTime.setText("Time's up!")
            font_size = 60 if self.is_enlarged else 30 # Adjust font size for Time's up message too
            self.clockTime.setFont(QFont('Sophia Pro Soft', font_size))
        else:
            mins, secs = divmod(self.time_left, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            self.clockTime.setText(time_format)
            font_size = 120 if self.is_enlarged else 60
            self.clockTime.setFont(QFont('Sophia Pro Soft', font_size))

        self.clockTime.setVisible(True)
        self.time_input_box.setVisible(False)


    def countdown(self):
        # ... (remains IDENTICAL) ...
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            self.update_display()
        elif self.timer_running and self.time_left == 0:
            self.timer_running = False
            self.timer.stop()
            self.is_time_up = True
            self.update_display()
            self.play_sound()


    def play_sound(self):
        # ... (remains IDENTICAL) ...
        try:
            if getattr(sys, 'frozen', False):
                script_dir = os.path.dirname(sys.executable)
            else:
                script_dir = os.path.dirname(os.path.abspath(__file__))

            ring_path = os.path.join(script_dir, 'ring.wav')
            if os.path.exists(ring_path):
                winsound.PlaySound(ring_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            else:
                print(f"ring.wav not found in {script_dir}, playing system sound.")
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS | winsound.SND_ASYNC)
        except NameError:
             print("Could not determine script directory, playing system sound.")
             winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS | winsound.SND_ASYNC)
        except Exception as e:
            print(f"Error playing sound: {e}")


    def reset_timer(self):
        # ... (remains IDENTICAL) ...
        print("Resetting timer...")
        self.timer.stop()
        self.time_left = self.initial_seconds
        self.paused = False
        self.timer_running = self.time_left > 0
        self.is_time_up = False
        self.switch_to_display_mode() # Ensure display mode is active
        self.update_display()
        # Add this condition to play sound on reset if started without args
        if self.started_without_args:
            self.play_sound()
        if self.timer_running:
            self.timer.start(1000)


    def toggle_pause(self):
        # ... (remains IDENTICAL) ...
        if self.is_time_up or self.is_input_mode:
             return

        self.paused = not self.paused
        if self.paused:
            self.timer_running = False
            self.timer.stop()
        else:
            if self.time_left > 0:
                 self.timer_running = True
                 self.timer.start(1000)
            else:
                 self.timer_running = False

        print(f"Timer Paused: {self.paused}, Running: {self.timer_running}")


    def eventFilter(self, watched, event):
        # ... (remains IDENTICAL) ...
        if watched == self.time_input_box and event.type() == event.Type.KeyPress:
            if event.key() == Qt.Key.Key_Escape:
                print("Escape pressed in input")
                self.switch_to_display_mode()
                return True
        return super().eventFilter(watched, event)


    def mousePressEvent(self, event):
        # ... (remains IDENTICAL) ...
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPos = event.globalPosition().toPoint()
        elif event.button() == Qt.MouseButton.RightButton:
            self.show_context_menu(event.globalPosition().toPoint())


    def mouseMoveEvent(self, event):
        # ... (remains IDENTICAL - still updates original_geometry when moved while small) ...
        if event.buttons() == Qt.MouseButton.LeftButton and self.dragPos:
            new_pos = self.pos() + event.globalPosition().toPoint() - self.dragPos
            self.move(new_pos)
            self.dragPos = event.globalPosition().toPoint()
            # --- Update original_geometry when moved while small ---
            if not self.is_enlarged:
                self.original_geometry = self.geometry()
            # -----------------------------------------------------------


    def mouseDoubleClickEvent(self, event):
        # ... (remains IDENTICAL to the multi-screen version) ...
        if self.is_input_mode:
            return

        screens = QApplication.screens()
        primary_screen = QApplication.primaryScreen()

        if not self.is_enlarged:
            # Calculate enlarged size based on initial proportions
            # Use self.initial_geometry.width/height() for base size
            new_width = int(self.initial_geometry.width() * 2)
            new_height = int(self.initial_geometry.height() * 2)

            target_screen = None
            # Check if more than one screen is detected
            if len(screens) > 1:
                # Try to find a screen that isn't the primary one
                for screen in screens:
                    if screen != primary_screen:
                        target_screen = screen
                        print(f"Found secondary screen: {screen.name()}")
                        break # Use the first secondary screen found

            if target_screen:
                # Center on the secondary screen
                print("Centering on secondary screen.")
                screen_geometry = target_screen.availableGeometry()
            else:
                # Center on the current screen (which is likely the primary if only one exists)
                print("Centering on current/primary screen.")
                current_screen = self.screen() or primary_screen # Fallback to primary
                if not current_screen: # Should not happen, but safety check
                     print("Error: Could not determine target screen.")
                     return
                screen_geometry = current_screen.availableGeometry()

            # Calculate the centered position on the chosen screen
            center_x = screen_geometry.x() + (screen_geometry.width() / 2)
            center_y = screen_geometry.y() + (screen_geometry.height() / 2)
            target_x = int(center_x - new_width / 2)
            target_y = int(center_y - new_height / 2)

            # Apply sizing and positioning
            self.setMinimumSize(max(100, new_width), max(50, new_height))
            self.setMaximumSize(screen_geometry.width(), screen_geometry.height())
            self.setGeometry(target_x, target_y, new_width, new_height)
            self.is_enlarged = True
            print(f"Enlarged and moved to: ({target_x}, {target_y}) on screen '{target_screen.name() if target_screen else (self.screen().name() if self.screen() else 'Unknown')}'")

        else: # Shrinking back
            print(f"Restoring to original size/position: {self.original_geometry}")
            # Restore size based on the *initial* geometry's dimensions
            orig_width = int(self.initial_geometry.width())
            orig_height = int(self.initial_geometry.height())
            self.setMinimumSize(orig_width, orig_height)
            self.setMaximumSize(orig_width, orig_height) # Reset max size too

            # Restore position and size from self.original_geometry
            # self.original_geometry is updated when moved while small
            self.setGeometry(self.original_geometry)
            self.is_enlarged = False

        # Update display font size and request repaint
        self.update_display()
        self.update()


    def show_context_menu(self, pos):
        # ... (remains IDENTICAL) ...
        contextMenu = QMenu(self)

        self.pause_action.setText("Resume Timer (Shift+Space)" if self.paused else "Pause Timer (Shift+Space)")
        can_pause_resume = not self.is_time_up and not self.is_input_mode and self.time_left > 0
        self.pause_action.setEnabled(can_pause_resume)
        self.reset_action.setEnabled(not self.is_input_mode)
        self.change_time_action.setEnabled(not self.is_input_mode)

        contextMenu.addAction(self.pause_action)
        contextMenu.addAction(self.reset_action)
        contextMenu.addSeparator()
        contextMenu.addAction(self.change_time_action)
        contextMenu.addAction(self.change_opacity_action)
        contextMenu.addAction(self.change_font_color_action)
        contextMenu.addSeparator()
        contextMenu.addAction(self.save_settings_action)
        contextMenu.addSeparator()
        contextMenu.addAction(self.close_action)

        contextMenu.exec(pos)


    def switch_to_input_mode(self):
        # ... (remains IDENTICAL) ...
        if self.is_input_mode: return

        print("Switching to input mode")
        self.timer.stop() # Stop timer explicitly when entering input mode
        self.is_input_mode = True
        self.clockTime.setVisible(False)
        self.time_input_box.setVisible(True)
        self.time_input_box.setText("")
        self.time_input_box.setFocus()


    def switch_to_display_mode(self):
        # ... (remains IDENTICAL) ...
        if not self.is_input_mode: return
        print("Switching to display mode")

        self.is_input_mode = False
        self.time_input_box.setVisible(False)
        self.clockTime.setVisible(True)
        self.setFocus() # Give focus back to main window for shortcuts

        if not self.paused and self.time_left > 0:
             self.timer_running = True
             self.timer.start(1000)
             print("Timer resumed after input.")
        else:
             self.timer_running = False
             print("Timer remains stopped/paused after input.")
        self.update_display() # Update display immediately


    def handle_time_input(self):
        # ... (remains IDENTICAL) ...
        input_text = self.time_input_box.text().strip().lower()
        new_seconds = -1

        if not input_text:
            print("Empty input, switching back.")
            self.switch_to_display_mode()
            return

        try:
            match = re.match(r"^(?:(\d+)\s*m)?\s*(?:(\d+)\s*s?)?$", input_text)
            match_ms = re.match(r"^m\s*(\d+)\s*s\s*(\d+)$", input_text)
            match_m = re.match(r"^m\s*(\d+)$", input_text)
            match_s = re.match(r"^s\s*(\d+)$", input_text)

            if match and (match.group(1) or match.group(2)):
                mins = int(match.group(1) or 0)
                secs = int(match.group(2) or 0)
                new_seconds = mins * 60 + secs
            elif match_ms:
                mins = int(match_ms.group(1))
                secs = int(match_ms.group(2))
                new_seconds = mins * 60 + secs
            elif match_m:
                new_seconds = int(match_m.group(1)) * 60
            elif match_s:
                new_seconds = int(match_s.group(1))

            if new_seconds >= 0:
                print(f"Setting time to {new_seconds} seconds")
                self.initial_seconds = new_seconds
                self.time_left = new_seconds
                self.is_time_up = False
                self.paused = False
                self.timer_running = self.time_left > 0
                self.switch_to_display_mode()
                if self.timer_running:
                    pass
                else:
                    self.timer.stop()
            else:
                print(f"Invalid time input format: {input_text}")
                self.switch_to_display_mode()

        except ValueError:
            print(f"Invalid number format in input: {input_text}")
            self.switch_to_display_mode()


    def open_opacity_sliders(self):
        # ... (remains IDENTICAL) ...
        if self.opacity_slider_window is None or not self.opacity_slider_window.isVisible():
            current_window_opacity_percent = int(self.windowOpacity() * 100)
            current_background_opacity_percent = int(self.background_alpha / 2.55)

            self.opacity_slider_window = OpacitySliderWindow(
                parent=self,
                initial_window_opacity=max(10, current_window_opacity_percent),
                initial_background_opacity=current_background_opacity_percent
            )
            self.opacity_slider_window.windowOpacityChanged.connect(self.set_window_opacity)
            self.opacity_slider_window.backgroundOpacityChanged.connect(self.set_background_opacity)
            self.opacity_slider_window.show()
        else:
            self.opacity_slider_window.raise_()
            self.opacity_slider_window.activateWindow()


    def change_font_color(self):
        # ... (remains IDENTICAL) ...
        color = QColorDialog.getColor(self.font_color, self, "Choose Font Colour")
        if color.isValid():
            self.font_color = color
            self.update_font_color_style()
            print(f"Font color changed to: {self.font_color.name()}")


    def save_settings(self):
        # --- MODIFICATION START ---
        # REMOVED saving geometry, as requested
        self.settings.setValue("initial_seconds", self.initial_seconds)
        self.settings.setValue("window_opacity", self.windowOpacity())
        self.settings.setValue("background_alpha", self.background_alpha)
        self.settings.setValue("font_color", self.font_color.name())
        # self.settings.setValue("geometry", self.original_geometry) # REMOVED
        self.settings.sync()
        print("Settings saved (excluding geometry).")
        # --- MODIFICATION END ---

    def close_app(self):
        # ... (remains IDENTICAL) ...
        print("Closing application...")
        if self.opacity_slider_window:
            self.opacity_slider_window.close()
        self.close() # Triggers closeEvent


    def closeEvent(self, event):
        # --- MODIFICATION START ---
        # Settings are saved, but geometry is excluded based on save_settings changes
        self.save_settings()
        # --- MODIFICATION END ---
        self.timer.stop()
        if self.opacity_slider_window:
             self.opacity_slider_window.close()
        print("Main window closeEvent")
        super().closeEvent(event)


# --- Main execution block remains the same ---
if __name__ == "__main__":
    # ... (remains IDENTICAL) ...
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)

    arg_seconds = None

    if len(sys.argv) == 1:
        arg_seconds = 0
        try:
            if getattr(sys, 'frozen', False):
                script_dir = os.path.dirname(sys.executable)
            else:
                script_dir = os.path.dirname(os.path.abspath(__file__))

            ring_path = os.path.join(script_dir, 'ring.wav')
            if os.path.exists(ring_path):
                winsound.PlaySound(ring_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            else:
                print(f"ring.wav not found in {script_dir}, playing system sound.")
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS | winsound.SND_ASYNC)
        except Exception as e:
            print(f"Error playing sound: {e}")

    elif len(sys.argv) > 1:
        timer_input = sys.argv[1].lower()
        try:
            temp_seconds = -1
            match = re.match(r"^(?:(\d+)\s*m)?\s*(?:(\d+)\s*s?)?$", timer_input)
            match_ms = re.match(r"^m\s*(\d+)\s*s\s*(\d+)$", timer_input)
            match_m = re.match(r"^m\s*(\d+)$", timer_input)
            match_s = re.match(r"^s\s*(\d+)$", timer_input)

            if match and (match.group(1) or match.group(2)):
                mins = int(match.group(1) or 0)
                secs = int(match.group(2) or 0)
                temp_seconds = mins * 60 + secs
            elif match_ms:
                mins = int(match_ms.group(1))
                secs = int(match_ms.group(2))
                temp_seconds = mins * 60 + secs
            elif match_m:
                temp_seconds = int(match_m.group(1)) * 60
            elif match_s:
                temp_seconds = int(match_s.group(1))

            if temp_seconds >= 0:
                arg_seconds = temp_seconds
            else:
                print(f"Warning: Could not parse argument '{sys.argv[1]}'. Using settings or 0.")
                arg_seconds = None
        except ValueError:
            print(f"Warning: Invalid number in argument '{sys.argv[1]}'. Using settings or 0.")
            arg_seconds = None

    window = CountdownTimer(initial_secs_from_arg=arg_seconds)
    window.show()
    sys.exit(app.exec())
