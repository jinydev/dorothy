#!/usr/bin/env python3
"""
generate_parts_dataset.py

Manages and generates 26 educational and environmental part assets for the Dorothy project:
- 01_environments: 6 backgrounds (lecture hall, workshop, workstation, fablab, server room, campus)
- 02_hardware: 8 components (Arduino, Raspberry Pi, breadboard, ultrasonic, temp, servo, DC motor, chassis)
- 03_software: 6 diagrams (Java OOP, PHP MVC, DB ERD, Docker, Web Dashboard, REST API)
- 04_ai_theory: 6 AI graphics (MLP neural net, CNN feature map, RL MDP, Bellman equation, Federated Learning, Loss curve)
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PARTS_DIR = BASE_DIR / "data" / "dataset" / "parts"

PARTS_REGISTRY = {
    "01_environments": [
        ("env_01_lecture_hall", "Studio Ghibli anime style, 2D animation aesthetic. A grand university lecture hall with tiered wooden seating, green chalkboard, smart projector screen, large sunny windows, architectural interior. Anime film background, crisp clean line art, no humans."),
        ("env_02_maker_workshop", "Studio Ghibli anime style, 2D animation aesthetic. A warm cozy maker robotics workshop with wooden workbench, pegboard filled with tools, parts organizer drawers, soldering station, breadboards. Afternoon sunlight streaming through window, no humans."),
        ("env_03_coding_workstation", "Studio Ghibli anime style, 2D animation aesthetic. A modern software engineering workstation with dual monitors showing VS Code editor, mechanical keyboard, coffee mug, engineering textbooks, desk lamp, warm inviting interior, no humans."),
        ("env_04_fablab_3d_printing", "Studio Ghibli anime style, 2D animation aesthetic. A high-tech FabLab maker room with desktop 3D printers, filament spool racks, workbench with small wooden robot models, acrylic gears, clean organized maker space, no humans."),
        ("env_05_ai_server_room", "Studio Ghibli anime style, 2D animation aesthetic. A compact edge AI server room with a server rack, a cluster of green Raspberry Pi nodes connected with blue ethernet cables and blinking green LEDs, clean futuristic lab, no humans."),
        ("env_06_campus_testing_ground", "Studio Ghibli anime style, 2D animation aesthetic. A beautiful sunny university campus lawn with lush green grass, wildflowers, paved pathways, and warm brick faculty buildings under a bright blue sky, outdoor testing field, no humans.")
    ],
    "02_hardware": [
        ("hw_01_arduino_uno", "Studio Ghibli anime style, 2D product illustration. Official cyan-blue Arduino Uno R3 microcontroller board, showing ATmega328P DIP chip, silver USB port, female pin headers, crystal oscillator. Isolated on pure white background, crisp anime line art."),
        ("hw_02_raspberry_pi_4", "Studio Ghibli anime style, 2D product illustration. Green Raspberry Pi 4 Model B single-board computer with metal CPU heatsink, dual micro-HDMI ports, USB 3.0 ports, ethernet jack, 40-pin GPIO header. Isolated on pure white background, clean anime line art."),
        ("hw_03_breadboard_circuit", "Studio Ghibli anime style, 2D technical illustration. White solderless breadboard with colorful rainbow jumper wires, blinking red and green LEDs, and ceramic resistors neatly wired in a working circuit. Isolated on pure white background, clean line art."),
        ("hw_04_ultrasonic_sensor", "Studio Ghibli anime style, 2D technical illustration. HC-SR04 ultrasonic distance sensor module with two round metal transducer cylinders resembling cute robot eyes on a blue PCB with 4-pin header. Isolated on pure white background, clean line art."),
        ("hw_05_dht11_temp_sensor", "Studio Ghibli anime style, 2D technical illustration. Blue DHT11 digital temperature and humidity sensor module with grid ventilation slats and 3-pin connection. Isolated on pure white background, crisp anime line art."),
        ("hw_06_servo_motor_sg90", "Studio Ghibli anime style, 2D technical illustration. Translucent blue TowerPro SG90 micro servo motor with white cross horn arm and three-strand control ribbon cable. Isolated on pure white background, crisp anime line art."),
        ("hw_07_dc_gear_motor_wheel", "Studio Ghibli anime style, 2D technical illustration. Yellow TT DC electric gearbox motor attached to a black rubber treaded robotics wheel. Isolated on pure white background, crisp anime line art."),
        ("hw_08_autonomous_car_chassis", "Studio Ghibli anime style, 2D technical illustration. Transparent acrylic 2-wheel robot car chassis with two drive wheels, battery compartment, and front caster ball wheel. Isolated on pure white background, crisp anime line art.")
    ],
    "03_software": [
        ("sw_01_java_oop_architecture", "Studio Ghibli anime style educational graphic. Java Object-Oriented Programming UML diagram showing inheritance hierarchy, interfaces, encapsulation, and polymorphism with clean arrows, plus a steaming coffee mug icon. Clean vector layout on white background."),
        ("sw_02_php_web_mvc", "Studio Ghibli anime style educational graphic. PHP web server architecture diagram showing HTTP request-response cycle and MVC pattern, accompanied by a cute purple elephant mascot illustration. Clean vector layout on white background."),
        ("sw_03_database_erd_schema", "Studio Ghibli anime style educational graphic. Database Entity Relationship Diagram (ERD) showing relational tables for MySQL and PostgreSQL, primary keys, foreign key arrows, and a B-Tree index visualization. Clean layout on white background."),
        ("sw_04_docker_containerization", "Studio Ghibli anime style educational graphic. Docker container architecture diagram with a friendly blue Docker whale carrying cargo containers, explaining container vs virtual machine layers. Clean vector layout on white background."),
        ("sw_05_web_telemetry_dashboard", "Studio Ghibli anime style technical graphic. Modern web telemetry dashboard with responsive JavaScript charts, live sensor line graphs, speedometer dials, and battery gauges in a clean dark-mode UI. Clean anime vector graphic on white background."),
        ("sw_06_rest_api_json_flow", "Studio Ghibli anime style educational graphic. RESTful API flow diagram illustrating client HTTP GET/POST requests and server JSON responses with formatted curly brackets. Educational textbook style on white background.")
    ],
    "04_ai_theory": [
        ("ai_01_neural_network_mlp", "Studio Ghibli anime style educational graphic. Multilayer perceptron artificial neural network diagram with input layer, hidden layers, and output layer with glowing interconnected nodes and synaptic weight lines. Clean anime line art on white background."),
        ("ai_02_cnn_feature_extraction", "Studio Ghibli anime style educational graphic. Convolutional Neural Network (CNN) feature extraction diagram showing convolution filter kernels sliding across an image, pooling layers, and feature maps. Clean layout on white background."),
        ("ai_03_reinforcement_learning_mdp", "Studio Ghibli anime style educational graphic. Reinforcement learning Markov Decision Process (MDP) feedback loop diagram showing the Agent, Environment, State, Action, and Reward cycle. Clear pedagogical diagram on white background."),
        ("ai_04_bellman_equation_chalk", "Studio Ghibli anime style. Close-up of a green university chalkboard with the Bellman Optimality Equation and Q-learning value function written neatly in white chalk, accompanied by small neural network diagrams. Academic anime still."),
        ("ai_05_federated_learning_arch", "Studio Ghibli anime style educational graphic. Federated Learning distributed architecture diagram showing a central server aggregating model weights from multiple edge Raspberry Pi client nodes without transferring raw data. Clean arrows on white background."),
        ("ai_06_training_loss_metrics", "Studio Ghibli anime style educational graphic. Machine learning training progress graph showing training loss curve descending over epochs and validation accuracy rising, with clean grid lines and data science labels on white background.")
    ]
}

def print_status():
    print("=======================================================")
    print("  Dorothy Universe: Parts & Theory Assets Status")
    print("=======================================================")
    total_expected = 0
    total_jpg = 0
    total_txt = 0
    for category, items in PARTS_REGISTRY.items():
        cat_dir = PARTS_DIR / category
        cat_dir.mkdir(parents=True, exist_ok=True)
        jpg_count = len(list(cat_dir.glob("*.jpg")))
        txt_count = len(list(cat_dir.glob("*.txt")))
        expected = len(items)
        total_expected += expected
        total_jpg += jpg_count
        total_txt += txt_count
        status = "READY FOR GENERATION" if jpg_count < expected else "COMPLETE"
        print(f"[{category}] {status}")
        print(f"   Images: {jpg_count:2d}/{expected:2d} | Captions (.txt): {txt_count:2d}/{expected:2d}")
    print("-------------------------------------------------------")
    print(f"Total Parts Assets: {total_jpg}/{total_expected} Images | {total_txt}/{total_expected} Captions")
    print("=======================================================")

if __name__ == "__main__":
    print_status()
