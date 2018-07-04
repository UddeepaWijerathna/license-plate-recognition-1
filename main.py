
from PlateRecognise import *;
import os;
import logging;
from logging.config import fileConfig;

fileConfig("logging_config.ini");
logger = logging.getLogger();


def run():

    plates_array = [];
    images_folder = "images/cars/";
    for image_filename in os.listdir(images_folder):
        logger.info("Loading image %s...", image_filename);
        image_file = cv2.imread(images_folder + image_filename);
        plateObject = PlateRecognise(image_file);
        plates_array.append(plateObject);



    for plate in plates_array:
        plate.plateSearch();

    logger.info("Finished plate recognition.");
    return True;


run();
