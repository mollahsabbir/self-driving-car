# Mode can be of type: "KEYBOARD", "SELFDRIVING" and "TRAIN"
GAME_MODE = "TRAIN"

TRACK_IMAGE = "assets/tracks/track1.png"

CAR_IMAGE = "assets/cars/skybluecar.png"
FPS = 60

START_POSITION_X = 880
START_POSITION_Y = 280
START_ROTATION_ANGLE = -90

CAR_MAX_SPEED = 5
CAR_ROTATION_SPEED = 2
CAR_ACCELERATION = 0.8
CAR_FRICTION = 0.2

OBSTACLE_COLOR = (255, 255, 255, 255)

SENSOR_SIZE = 150
SENSOR_COLOR = (255, 255, 0, 255)
SENSOR_ACTIVE_COLOR = (0, 0, 255, 255)
SENSOR_ANGLES = [-60, -30, 0, 30, 60]

TRAIN_CARS_NUMBER = 100
SECONDS_PER_GENERATION = 60
MUTATION_AMOUNT = 0.5
MODEL_LOCATION = "model/best_model.pickle"
BACKUP_MODEL_LOCATION = "model/backup_best_model.pickle"
# Input of the neural network is equal to
# the number of sensors
# Output size is 4: Forward, Reverse, Left, Right
NN_LAYERS_DIMS = [len(SENSOR_ANGLES), 10, 4]