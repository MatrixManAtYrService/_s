# `_s`
(a.k.a fluoresce)

![green fluorescent protein glowing on an agar plate](shroom.png)

Fluoresce is a tool for annotating text data.

## Usage

### Gallery Mode

Stores canvases and brushstrokes in `~/.fluoresce`.


```bash
$ echo 'hello world' | _s --paint
    no canvas found for sha256:22596363b3de40b06f981fb85d82312e8c0ed511

    ... a TUI launches which you use color 'h' green and 'w' blue ...

    _s wrote:
    { "brushstrokes" : "/home/user/._s/paint/22/59/6363b3de40b06f981fb85d82312e8c0ed511.json",
      "canvas" : "/home/user/._s/canvas/22/59/6363b3de40b06f981fb85d82312e8c0ed511" }

$ echo 'hello world' | _s --query

    {
      "path": "/home/user/._s/paint/22/59/6363b3de40b06f981fb85d82312e8c0ed511" }
      "indices" : { "green" : [0, 1], "blue": [6, 7] },
      "substrings" : { "green" : "h", "blue": "w" },
      "canvas": { "sha256": "22596363b3de40b06f981fb85d82312e8c0ed511", 
                  "path": "/home/user/._s/canvas/22/59/6363b3de40b06f981fb85d82312e8c0ed511" }
    }

$ echo 'hello world' | _s

    hello world  # green: 'h'; blue: 'w'
```

### Regex Mode

Ignores `~/._s` and just applies color based on regex supplied by the caller.

```
$ echo 'hello world' | _s '#00ff0000=.l' '#0000ff00=^he'

    hello world  # green: 'he'; red: 'ell', 'rl'
```
