from PIL import ImageColor

# --- Instagram Post Dimensions ---
# Standard square post size
POST_WIDTH = 1080
POST_HEIGHT = 1080

# --- Colors ---
# Instagram text looks best with a strong yellow, and a solid black gradient
TEXT_COLOR = ImageColor.getrgb("#FFD700")  # Vibrant Gold/Yellow
GRADIENT_START = (0, 0, 0, 230)            # Dark black (bottom) - Alpha 230/255
GRADIENT_END = (0, 0, 0, 0)                # Fully transparent (top)

# --- Typography ---
FONT_PATH = "content/fonts/Creator_Genius.ttf"         # Path to your TTF font
FONT_SIZE = 64                             # Adjust based on preference
LINE_SPACING = 15                          # Pixel spacing between wrapped text lines

# --- Layout ---
PADDING_X = 80                             # Left/Right margins for text
PADDING_BOTTOM = 100                       # Distance from the bottom of the image
GRADIENT_HEIGHT_PCT = 0.65                 # Gradient covers bottom 65% of the image

# Image settings
IMAGE_WIDTH = 1080
IMAGE_HEIGHT = 1080
FONT_TITLE = "assets/fonts/bold.ttf"
BACKGROUND_TEMPLATES_DIR = "assets/templates/"
OUTPUT_IMAGES_DIR = "output/images/"



