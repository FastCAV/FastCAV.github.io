# Improvements

## Resize images

1. Resize image with `convert` to 500px in width

```bash
convert b.png -resize 500x b_r.png 
```

2. Convert to `webp` format

```bash
cwebp -q 100 b_r.png -o b_web.webp
```
