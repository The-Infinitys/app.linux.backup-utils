from include import *

class InfinitySnapshotManager(App):
    CSS=""""""
    ENABLE_COMMAND_PALETTE=False
    BINDINGS = [
      ("q", "quit_app()", "Quit the application"),
      ]
    def compose(self) -> ComposeResult:
        # Compose the UI
        yield Header("The Infinity's SnapShot Manager")
        yield Footer()        
    def on_mount(self) -> None:
        # Initialize the theme
        infinite_theme = Theme(
          name="infinite",
          primary="#999999",
          secondary="#3333FF",
          accent="#11FFFF",
          foreground="#EEEEEE",
          background="#111111",
          success="#00FFFF",
          warning="#FFFF00",
          error="#FF0000",
          surface="#000000",
          panel="#333333",
          dark=True,
          variables={
              "block-cursor-text-style": "none",
              "footer-key-foreground": "#00ffff",
          },
        )
        # Register the theme
        self.register_theme(infinite_theme)
        self.theme = "infinite"

    def action_quit_app(self) -> None:
        self.exit(0)

# Run the application
if __name__ == "__main__":  
    app = InfinitySnapshotManager()
    app.run()
