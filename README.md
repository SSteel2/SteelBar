# SteelBar
Simple python multilayered progress bar for console applications.

If multiple instances are created, they will stack on top of each other.

To use:
  1. Import
    import steelbar
  
  2. Create instance with iteration count and optional flavor text for easier progress tracking.
    progress = steelbar.SteelBar(iterations, 'Processing happy ducks')
    
  3. Increment with each iteration
    progress.Increment()
