#!/usr/bin/env python3
"""
generate_robot_dataset.py

Manages and generates 20 visual dataset assets for the 5th character:
Robot 'Tinny' (Tin Woodman / OzBot) in the Dorothy Project.
Focuses on AI, reinforcement learning, robotics, and maker lab interactions.
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ROBOT_DIR = BASE_DIR / "data" / "dataset" / "robot"

ROBOT_REGISTRY = [
    (
        "robot_01",
        "Tinny Front Standing",
        "Studio Ghibli style, 2D anime aesthetic, clean line art, soft warm pastel colors, cell shaded. 1robot named Tinny, small cute humanoid maker robot standing facing front on a clean white background. Retro rounded rectangular monitor head with glowing cyan-blue dot-matrix LED eyes, small coiled brass spring antenna with warm yellow tiny lightbulb tip. Matte tin-silver cylindrical torso and limbs with brass bolts and servo joints, 3-finger hands. Transparent circular glass chest window with glowing warm amber-orange heart core of brass cogwheels. Full body, endearing friendly expression."
    ),
    (
        "robot_02",
        "Tinny Side Turnaround",
        "Studio Ghibli style, 2D anime aesthetic, clean line art, soft cel shading. 1robot named Tinny, small cute maker robot in full body side profile view on white background. Matte silver chassis, brass shoulder and knee joints, rear modular rechargeable battery pack with small power indicator LEDs, curved posture."
    ),
    (
        "robot_03",
        "Tinny Face Portrait Close-up",
        "Studio Ghibli style, 2D anime portrait, soft lighting, clean line art. Close-up headshot of Tinny the cute robot on clean background. Retro monitor faceplate, glowing sky-blue LED dot matrix eyes shaped like happy smiling crescents, brass spring antenna with warm yellow glowing lightbulb."
    ),
    (
        "robot_04",
        "Glowing Heart Core Close-up",
        "Studio Ghibli style, 2D anime detail illustration. Extreme close-up of Tinny robot's chest window on white background. Transparent circular glass revealing a glowing warm golden-amber heart core made of intricate interlocking brass gears and tiny copper cogs pulsing with life."
    ),
    (
        "robot_05",
        "Curious Head Tilt",
        "Studio Ghibli style, 2D anime character art, clean lines, soft cel shading. 1robot named Tinny with head tilted cutely to one side in deep curiosity on white background. LED dot matrix eyes displaying a digital question mark and exclamation mark, brass hands raised to chin in thinking gesture."
    ),
    (
        "robot_06",
        "Friendly Waving Welcome Pose",
        "Studio Ghibli style, 2D anime character art, cheerful atmosphere. 1robot named Tinny waving one 3-finger metallic hand warmly at the viewer on clean white background. Happy curved LED eyes, upright spring antenna, glowing amber heart core, welcoming greeting stance."
    ),
    (
        "robot_07",
        "RL First Steps Wobble",
        "Studio Ghibli anime style, 2D animation frame. 1robot named Tinny taking its very first bipedal walking steps on the polished wooden floor of a robotics lab. Arms outstretched sideways trying to balance, knees slightly bent, intense concentration on its blue LED eyes, reinforcement learning trial."
    ),
    (
        "robot_08",
        "Fallen Down Bump Reaction",
        "Studio Ghibli anime style, 2D comic animation still. 1robot named Tinny sitting bumped on the floor after a walking fall. Swirling spiral doodle LED eyes in slight comical dizziness, one hand rubbing its rounded monitor head, glowing heart pulsing gently, resilient spirit."
    ),
    (
        "robot_09",
        "Standing Up Determined",
        "Studio Ghibli anime style, 2D animation frame. 1robot named Tinny pushing both hands firmly against the floor, determinedly getting back onto its feet. Resolute bright LED eyes, brass joints flexing, learning from failure, inspirational robot training."
    ),
    (
        "robot_10",
        "One-Leg Balance Success",
        "Studio Ghibli anime style, 2D animation art. 1robot named Tinny successfully balancing perfectly on one foot on a workshop workbench, arms spread like wings in triumphant joy. Sparkling star-shaped LED eyes, yellow antenna lightbulb glowing brightly."
    ),
    (
        "robot_11",
        "High-Five with Dorothy",
        "Studio Ghibli anime style, warm daylight laboratory. Dorothy with brown braided pigtails in blue overalls and Tinny the small silver maker robot doing a high-five together over a wooden desk. Shared joy, partnership, warm emotional connection between human and AI."
    ),
    (
        "robot_12",
        "Robot & Toto Observing Car",
        "Studio Ghibli anime style, warm cozy robotics lab floor. Tinny the silver robot crouching down side-by-side with Toto the scruffy golden-brown terrier. Both eagerly watching a miniature 2-wheeled autonomous robotic car drive along a yellow tape track."
    ),
    (
        "robot_13",
        "Jiny Cat Loaf on Robot Head",
        "Studio Ghibli anime style, humorous and cozy scene. Tinny the cute silver robot sitting still while Jiny the black and white tuxedo cat sleeps peacefully curled in a bread-loaf pose directly on top of the robot's flat monitor head. Tinny's LED eyes glancing upward comically."
    ),
    (
        "robot_14",
        "Charging Dock Sleep Mode",
        "Studio Ghibli anime style, quiet nighttime laboratory scene with moonlight. Tinny the small maker robot sitting peacefully in a wooden charging dock, connected by a vintage braided power cable. LED eyes showing a soft gentle sleeping straight line, heart core pulsing dim warm amber."
    ),
    (
        "robot_15",
        "Idea Lightbulb Eureka",
        "Studio Ghibli anime style, lively 2D art. 1robot named Tinny having a sudden eureka idea on white background. Yellow miniature lightbulb on top of head glowing with bright radiant anime light rays, arms raised in excitement, glowing heart core beating fast."
    ),
    (
        "robot_16",
        "Self-Maintenance Screwdriver",
        "Studio Ghibli anime style, maker workbench scene. Tinny the silver robot holding a small precision screwdriver in its 3-finger hand, carefully tightening a brass bolt on its own knee joint. Breadboards, soldering iron, and spare resistors scattered around."
    ),
    (
        "robot_17",
        "RL Math Mentoring with Hojin",
        "Studio Ghibli anime style, university lecture room. Professor Hojin in brown tweed vest pointing at the Bellman Equation written in chalk on a large green blackboard, explaining value iteration to Tinny the robot who looks up attentively taking notes."
    ),
    (
        "robot_18",
        "GridWorld Maze Navigation",
        "Studio Ghibli anime style, robotics testing area. Tinny the small robot carefully stepping through a colorful gridworld maze mat laid out on the floor, analyzing ultrasonic sensor distance to obstacle blocks, glowing path."
    ),
    (
        "robot_19",
        "Happy Victory Dance",
        "Studio Ghibli anime style, energetic 2D animation frame. Tinny the robot performing an adorable celebratory victory dance on white background, arms swinging playfully, happy smiling crescent LED eyes, heart core radiating bright warm amber light."
    ),
    (
        "robot_20",
        "Full Dorothy Team Lab Scene",
        "Studio Ghibli anime style, masterpiece university laboratory scene. The complete 5-member team: Professor Hojin holding lecture notes, Dorothy in overalls smiling proudly, Jiny the tuxedo cat perched on a textbook, Toto the terrier wagging tail, and Tinny the silver robot standing front and center holding a small glowing neural network crystal."
    )
]

def print_status():
    print("=======================================================")
    print("  Dorothy Universe: Robot 'Tinny' Dataset Status")
    print("=======================================================")
    
    total = len(ROBOT_REGISTRY)
    jpg_count = 0
    txt_count = 0
    
    for item_id, title, prompt in ROBOT_REGISTRY:
        jpg_path = ROBOT_DIR / f"{item_id}.jpg"
        txt_path = ROBOT_DIR / f"{item_id}.txt"
        
        has_jpg = jpg_path.exists()
        has_txt = txt_path.exists()
        
        if has_jpg:
            jpg_count += 1
        if has_txt:
            txt_count += 1
            
        status = "✅ READY" if has_jpg and has_txt else ("📝 TXT ONLY" if has_txt else "❌ MISSING")
        print(f"[{status:^11}] {item_id:8} | {title:30}")
        
    print("-------------------------------------------------------")
    print(f"Total Registry Items : {total}")
    print(f"Completed JPG Images : {jpg_count} / {total} ({(jpg_count/total)*100:.1f}%)")
    print(f"Completed TXT Labels : {txt_count} / {total} ({(txt_count/total)*100:.1f}%)")
    print("=======================================================")

if __name__ == "__main__":
    print_status()
