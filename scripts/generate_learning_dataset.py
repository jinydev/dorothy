#!/usr/bin/env python3
"""
generate_learning_dataset.py

Manages and generates learning dataset images and 1:1 matching LoRA .txt captions
for Dorothy, Prof. Hojin, TA Jiny, and Toto across 14 technology domains:
- Artificial Intelligence & Deep Learning
- Reinforcement Learning & Federated Learning
- Python, JavaScript, Java, PHP
- Arduino & Raspberry Pi
- MySQL & PostgreSQL
- Docker & Linux CLI
"""

import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "data" / "dataset"

# 1. Toto Remaining (17-20)
TOTO_REMAINING = [
    {
        "id": "toto_17",
        "output_dir": DATASET_DIR / "toto",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic, single subject, no text, no labels, no watermark. Toto the Maker Puppy standing up on its hind legs (cute begging / prairie dog pose!). Both front fluffy paws folded softly in front of chest, balancing happily on two rear feet, tail wagging upward like a cotton puff. Sparkling big round black eyes, black button nose, joyful open mouth with pink tongue. Fluffy cream-white wavy fur, sky-blue bandana around neck. Clean simple solid white background, high quality anime vector style art.",
        "caption": "1dog, toto, puppy, bichon frise, maltese, fluffy dog, white dog, cream dog, wavy fur, floppy ears, standing on hind legs, begging, prairie dog pose, open mouth, tongue, happy, smiling, big black eyes, black nose, blue bandana, neckerchief, simple background, white background, anime style, ghibli aesthetic, clean line art\n"
    },
    {
        "id": "toto_18",
        "output_dir": DATASET_DIR / "toto",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic, single scene, no text, no labels, no watermark. Toto the Maker Puppy on a wooden workshop workbench, curiously sniffing a bright colorful acrylic gear cogwheel with its wet black button nose. Fluffy cream-white wavy fur, floppy ears, sparkling black eyes, sky-blue bandana around neck. In the background are breadboard circuits, miniature motors, and tools in soft cozy focus. High quality anime vector style art.",
        "caption": "1dog, toto, puppy, bichon frise, maltese, fluffy dog, white dog, cream dog, wavy fur, floppy ears, sniffing, acrylic gear, cogwheel, workbench, maker workshop, breadboard, leds, tools, blue bandana, neckerchief, curious, anime style, ghibli aesthetic, clean line art\n"
    },
    {
        "id": "toto_19",
        "output_dir": DATASET_DIR / "toto",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic, single scene, no text, no labels, no watermark. Toto the Maker Puppy sitting happily in a sunny green meadow with colorful wildflowers, a gentle spring breeze softly blowing through its fluffy cream-white wavy fur. Bright joyful puppy smile with pink tongue out, sparkling black eyes, black button nose, sky-blue bandana fluttering. Warm golden sunlight, peaceful and heartwarming anime landscape. High quality anime vector style art.",
        "caption": "1dog, toto, puppy, bichon frise, maltese, fluffy dog, white dog, cream dog, wavy fur, floppy ears, sitting, meadow, green grass, wildflowers, sunny day, breeze, wind blowing fur, open mouth, tongue, happy, smiling, blue bandana, neckerchief, outdoor, anime style, ghibli aesthetic, clean line art\n"
    },
    {
        "id": "toto_20",
        "output_dir": DATASET_DIR / "toto",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic, single subject, no text, no labels, no watermark. Toto the Maker Puppy caught in a dynamic mid-air leap, catching a soft yellow toy gear in its mouth! All four paws outstretched in airborne motion, fluffy tail flying behind, floppy ears fluttering. Fluffy cream-white wavy fur, joyful excited eyes, sky-blue bandana fluttering. Dynamic action lines, clean simple solid white background, high quality anime vector style art.",
        "caption": "1dog, toto, puppy, bichon frise, maltese, fluffy dog, white dog, cream dog, wavy fur, floppy ears, jumping, leaping, mid-air, airborne, catching toy, gear toy, paws extended, flying tail, happy, excited, blue bandana, neckerchief, motion lines, simple background, white background, anime style, ghibli aesthetic, clean line art\n"
    }
]

# 2. Technology Learning Expansion Dataset (20 items)
TECH_LEARNING_DATASET = [
    {
        "id": "dorothy_learn_01_raspberry_pi",
        "output_dir": DATASET_DIR / "dorothy",
        "topic": "Raspberry Pi & Edge AI",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic. Dorothy at her maker desk inspecting a green Raspberry Pi board connected to a small camera module and small display showing real-time object detection bounding boxes. Wearing denim overalls with STEM HERO badge and orange striped shirt. Cheerful curious expression. Cozy electronics maker lab background.",
        "caption": "1girl, dorothy, raspberry pi, camera module, edge ai, computer vision, bounding boxes, electronic display, maker lab, overalls, orange striped shirt, amber eyes, pigtails, anime style, ghibli aesthetic, clean line art\n"
    },
    {
        "id": "dorothy_learn_02_federated_learning",
        "output_dir": DATASET_DIR / "dorothy",
        "topic": "Federated Learning",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic. Dorothy sitting before a cluster of three small Raspberry Pi single-board computers interconnected by blue ethernet cables, watching a decentralized federated learning loss graph on a computer screen. Jiny the tuxedo cat with glasses sits next to the monitor inspecting the weights. Warm academic robotics lab.",
        "caption": "1girl, dorothy, federated learning, raspberry pi cluster, decentralized network, ethernet cables, loss graph, 1cat jiny, glasses, maker lab, overalls, pigtails, anime style, ghibli aesthetic, clean line art\n"
    },
    {
        "id": "hojin_teach_01_federated_averaging",
        "output_dir": DATASET_DIR / "hojin",
        "topic": "Federated Averaging (FedAvg)",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic. Professor Hojin in his dark navy polo shirt and blue jeans, standing at a classroom chalkboard, writing mathematical formulas for Federated Averaging (FedAvg) and drawing distributed edge client nodes with white chalk. Turning to smile with inspiring academic mentorship. Clean anime vector art.",
        "caption": "1man, hojin, professor, mature male, dark navy polo shirt, blue jeans, glasses, short hair, chalkboard, blackboard, writing with chalk, federated learning, fedavg formula, distributed clients, lecture hall, warm smile, anime style, ghibli aesthetic\n"
    },
    {
        "id": "dorothy_learn_03_docker_containers",
        "output_dir": DATASET_DIR / "dorothy",
        "topic": "Docker & Containerization",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic. Dorothy sitting at a modern dual-monitor developer desk, cheering joyfully with both arms raised in celebration as a Docker container build finishes with a cute blue Docker whale on screen next to Python FastAPI code. Jiny the cat watches from beside the keyboard with approval. Warm developer workstation.",
        "caption": "1girl, dorothy, cheering, hands up, happy, celebrating, docker, docker whale, container build, terminal, python code, dual monitor, developer desk, overalls, pigtails, anime style, ghibli aesthetic, clean line art\n"
    },
    {
        "id": "jiny_review_01_dockerfile",
        "output_dir": DATASET_DIR / "jiny",
        "topic": "Dockerfile Code Review",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic. Jiny the Lab Assistant Cat sitting on an office desk, peering intently through round metal spectacles at a computer screen showing Dockerfile layers and multi-stage build instructions, one white paw pointing at the cache optimization line. Serious and adorable technical code review.",
        "caption": "1cat, jiny, tuxedo cat, black and white cat, glasses, round spectacles, paw pointing, code review, dockerfile, terminal screen, developer desk, red collar, bell on collar, focused, intelligent, anime style, ghibli aesthetic\n"
    },
    {
        "id": "dorothy_learn_04_linux_cli",
        "output_dir": DATASET_DIR / "dorothy",
        "topic": "Linux CLI & Bash",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic. Dorothy typing focusedly on a mechanical keyboard in front of a dark terminal screen displaying green Linux command line text and bash scripts. Wearing her signature denim overalls and orange striped shirt. Soft glow from the monitor on her face. Cozy nighttime lab setting.",
        "caption": "1girl, dorothy, typing, keyboard, linux terminal, green text, bash script, dark mode, glowing screen, overalls, pigtails, focused expression, amber eyes, night lab, anime style, ghibli aesthetic, clean line art\n"
    },
    {
        "id": "dorothy_learn_05_mysql_erd",
        "output_dir": DATASET_DIR / "dorothy",
        "topic": "MySQL & Relational Database",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic. Dorothy standing in front of a large whiteboard, drawing an Entity Relationship Diagram (ERD) with relational tables, primary keys, and foreign key connections using colorful dry-erase markers. An open MySQL textbook sits on the desk nearby. Thoughtful, enthusiastic smile.",
        "caption": "1girl, dorothy, whiteboard, drawing erd, relational database, mysql, table schema, foreign keys, colorful markers, overalls, pigtails, smiling, anime style, ghibli aesthetic, clean line art\n"
    },
    {
        "id": "dorothy_learn_06_postgresql_queries",
        "output_dir": DATASET_DIR / "dorothy",
        "topic": "PostgreSQL & Advanced SQL",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic. Dorothy seated before a large computer display analyzing PostgreSQL SQL queries and execution plans with EXPLAIN ANALYZE, comparing JSONB and relational queries. Professor Hojin stands beside her with a hand on the chair back, pointing encouragingly at the query plan.",
        "caption": "1girl, dorothy, 1man hojin, postgresql, database query, explain analyze, execution plan, sql query, mentoring, lab desk, dual screens, overalls, navy polo shirt, anime style, ghibli aesthetic\n"
    },
    {
        "id": "dorothy_learn_07_java_oop",
        "output_dir": DATASET_DIR / "dorothy",
        "topic": "Java & Object-Oriented Programming",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic. Dorothy sitting at a study desk drawing Java object-oriented class inheritance and interface diagrams on a transparent glass board. A Java engineering manual and a warm ceramic mug with a coffee bean emblem rest on the table. Intelligent, curious learner vibe.",
        "caption": "1girl, dorothy, java oop, object oriented programming, glass board, class hierarchy, interfaces, spring boot book, ceramic mug, overalls, pigtails, anime style, ghibli aesthetic, clean line art\n"
    },
    {
        "id": "dorothy_learn_08_php_migration",
        "output_dir": DATASET_DIR / "dorothy",
        "topic": "PHP & Modern Web Refactoring",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic. Dorothy comparing legacy PHP server code on the left half of a widescreen monitor with modern Python FastAPI REST endpoints on the right half, holding her chin in deep concentration with an excited maker smile. A small purple elephant plush toy sits on the monitor riser.",
        "caption": "1girl, dorothy, code refactoring, php, python fastapi, split screen, code comparison, chin on hand, thoughtful, purple elephant mascot, overalls, pigtails, developer desk, anime style, ghibli aesthetic\n"
    },
    {
        "id": "dorothy_learn_09_javascript_dashboard",
        "output_dir": DATASET_DIR / "dorothy",
        "topic": "JavaScript & Interactive Web UI",
        "prompt": "Studio Ghibli anime style, 2D animation aesthetic. Dorothy viewing an interactive real-time JavaScript robotics web dashboard with responsive charts, sensor telemetry gauges, and an interactive 3D model. Glowing screen lights up her face with wonder. Modern clean web engineering room.",
        "caption": "1girl, dorothy, javascript, web dashboard, real time telemetry, charts, interactive ui, glowing monitor, wonder, overalls, pigtails, amber eyes, maker lab, anime style, ghibli aesthetic, clean line art\n"
    }
]

def check_dataset_status():
    """Prints current dataset status."""
    print("=== Dorothy Universe LoRA Dataset Status ===")
    for char in ["dorothy", "hojin", "jiny", "toto"]:
        char_dir = DATASET_DIR / char
        jpgs = list(char_dir.glob("*.jpg"))
        txts = list(char_dir.glob("*.txt"))
        print(f"  [{char.upper():<7}] Images: {len(jpgs):2d} | Captions: {len(txts):2d}")

if __name__ == "__main__":
    check_dataset_status()
    print(f"\nPlanned toto remaining images: {len(TOTO_REMAINING)}")
    print(f"Planned tech learning expansion images: {len(TECH_LEARNING_DATASET)}")
