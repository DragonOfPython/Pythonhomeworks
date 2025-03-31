from PIL import Image
import numpy as np
import random

# Read the image using PIL
image = Image.open("images/birds.jpg")
image_array = np.array(image)

def save_image(image_array, filename):
    # Convert the modified NumPy array back to an image and save it
    modified_image = Image.fromarray(image_array.astype('uint8'))
    modified_image.save(filename)

def flip_image(image_array):
    # Flip the image horizontally and vertically
    flipped_lr = np.fliplr(image_array)
    flipped_ud = np.flipud(image_array)
    return flipped_lr, flipped_ud

def add_noise(image_array):
    # Add random noise to the image
    noise = np.random.randint(0, 50, image_array.shape)
    noisy_image = np.clip(image_array + noise, 0, 255)
    return noisy_image

def brighten_channels(image_array, value=40):
    # Increase the brightness of the channels by a fixed value
    brightened_image = np.clip(image_array + value, 0, 255)
    return brightened_image

def apply_mask(image_array, x=100, y=100, width=100, height=100):
    # Apply a mask to a rectangular region in the image
    masked_image = image_array.copy()
    masked_image[y:y+height, x:x+width] = [0, 0, 0]
    return masked_image

# Flip the image horizontally and vertically
flipped_lr, flipped_ud = flip_image(image_array)

# Add random noise to the image
noisy_image = add_noise(image_array)

# Increase the brightness of the channels by a fixed value
brightened_image = brighten_channels(image_array, value=40)

# Apply a mask to a rectangular region in the image
masked_image = apply_mask(image_array, x=100, y=100, width=100, height=100)

# Save the modified images
save_image(flipped_lr, "flipped_lr.jpg")
save_image(flipped_ud, "flipped_ud.jpg")
save_image(noisy_image, "noisy_image.jpg")
save_image(brightened_image, "brightened_image.jpg")
save_image(masked_image, "masked_image.jpg")