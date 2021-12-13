from gimpfu import *

def stickerfy(image, stickerLayer, interpolation, borderColor):

    pdb.gimp_context_set_interpolation(interpolation)
    pdb.gimp_context_set_foreground(borderColor)
    if pdb.gimp_drawable_is_indexed(stickerLayer):
        pdb.gimp_image_convert_rgb(image)
    for layer in image.layers:
        pdb.gimp_image_set_active_layer(image, layer)
        pdb.plug_in_autocrop_layer(image, layer)
    pdb.gimp_image_resize_to_layers(image)
    for layer in image.layers:
        pdb.gimp_layer_resize_to_image_size(layer)
register(
    "stickerfy",
    "Makes pngs/gifs take on a sticker format described by WhatsApp best practices.",
    "Scale to 512x512, add margins, border and dropshadow.",
    "rud___boy",
    "rud___boy",
    "2019-2021",
    "<Image>/Filters/Plug-ins/_Stickerfy...",
    "RGB*, GRAY*, INDEXED",
    [
        (PF_RADIO, "interpolation", "Set interpolation method", 3,
            (
                ("None (for pixelart)", 0),
                ("LoHalo", 3),
                ("NoHalo", 4)
            )
        ),
        (PF_COLOR, "borderColor", "Set the border color", (255, 255, 255))
    ],
    [],
    stickerfy
)

main()
