# SteelBar
Simple python 3 multilayered progress bar for console applications.

## Installing

```
pip install steelbar
```

## Usage

1. Import

  ```python
  import steelbar
  ```
  
2. Create instance with iteration count and optional flavor text for easier progress tracking.

  ```python
  progress = steelbar.SteelBar(iterations, 'Processing happy ducks')
  ```
    
3. Increment with each iteration

  ```python
  progress.Increment()
  ```

If multiple instances are created, they will stack on top of each other.
