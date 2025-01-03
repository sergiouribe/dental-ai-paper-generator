from flask import Flask, render_template, jsonify
import random

# Data extracted from the uploaded text file
sections = {
    "Introduction": [
        "Revolutionize healthcare and dentistry",
        "Disrupt traditional diagnostic methods",
        "Enhance precision in treatment planning",
        "Simplify complex workflows in dental practices",
        "Accelerate research in oral health sciences",
        "Improve patient outcomes through predictive models",
        "Redefine dental education methodologies",
        "Transform oral health monitoring and prevention",
        "Personalize treatment pathways for patients",
        "Bridge gaps in underserved dental care"
    ],
    "Methods": [
        "Convolutional Neural Networks (CNNs)",
        "YOLOv7",
        "YOLOv8",
        "DeepDentalNet",
        "AI-DentProNet",
        "MolarVisionNet",
        "ToothDetect-XL",
        "OralCareGAN",
        "NeuralSmile 3.0",
        "PerioNet++",
        "BiteMarkNet",
        "SmartScanNet",
        "RootDetectAI",
        "DentGAN-4",
        "PlaqueNet Ultra"
    ],
    "For the": [
        "Segmentation of the occlusal face of the first upper premolar",
        "Diagnosis of periodontal status of the second molar distal in people traveling to Antarctica",
        "Detection of the disc pixel grey colors in panoramic images found in the hospital dump",
        "Halitosis scale derived from patient records, annotated by whoyouknowwho",
        "Caries status of the first molar annotated by three guys in a room with no windows",
        "Classification of third molar eruption stages in photos taken by dental students during karaoke nights",
        "AI-based detection of calculus on incisors in selfies uploaded to Instagram with #nofilter",
        "Prediction of crown fractures in dental mannequins after simulated alien abductions",
        "Identification of oral cancer risk based on fortune cookie messages from dental conferences",
        "Annotation of root canal morphology using random sketches submitted to TikTok challenges"
    ],
    "Dataset": [
        "Not available",
        "Not available, but available under reasonable requests",
        "Not available, but available under reasonable reason request",
        "Available, but only if you request using a letter with the stamp of the airplane inverted"
    ],
    "Code": [
        "Not available",
        "Not available, but available under reasonable requests",
        "Not available, but available under reasonable reason request",
        "We can't promise we'll try to provide it, but we'll try to try.",
        "Partially available, but key functions are missing due to 'technical limitations'"
    ],
    "Validation": [
        "The same dataset",
        "The same dataset in a different order",
        "The same dataset, but we changed from uppercase to lowercase the names of the files",
        "The same dataset, but only the images taken on Mondays",
        "The same dataset, but annotated by a cat walking on a keyboard",
        "The same dataset, but is now called a \"validation dataset\""
    ],
    "Results": [
        "The inverse of sensibility, that we now called \"sensible recall\" achieved a 0.99",
        "We combined Dice with F1 and a RTP (no ones remember what this means) achieving an almost perfect score of 0.999",
        "A recall-recall (RR) of 0.9997, validated by unanimous applause",
        "A novel metric called 'Accuracy Beyond Truth' (ABT) scoring 0.95, redefining perfection",
        "A 'Neural Fantastic Ratio' (NFR) of 0.98, computed during a coffee break",
        "An \"AI Enthusiasm Index\" (AIEI) of 99.5%, proving the model is not just good but also highly motivated",
        "A \"Deep Dental Determination Score\" (DDDS) of 0.97, validated by sheer confidence",
        "A metric known as 'Recallish Recall,' achieving an unprecedented 0.99±0.01",
        "The groundbreaking 'WOW (Wheels of Wisdom) Index' of 0.999"
    ],
    "Discussion": [
        "These results surpass any expectation, and we are sure of their clinical applications—if more, but good and real research is done.",
        "This study sets a new benchmark for AI research, provided someone else does the heavy lifting to verify our claims.",
        "Our findings are revolutionary and will transform clinical practice—pending confirmation by someone with better data, methods and everything else.",
        "These results validate the potential of AI, as long as future research adds a touch of reality to our optimistic conclusions.",
        "We believe this approach could have tremendous clinical value, assuming anyone ever reproduces it under rigorous conditions.",
        "Our results strongly suggest clinical applicability, as long as future work addresses the glaring limitations we conveniently ignored.",
        "These findings could redefine dentistry, but only if someone else figures out how to make them actually work.",
        "We are confident these results will inspire future studies to actually do the hard work we only pretended to do.",
        "This study is a game-changer, provided the game is played in an alternate universe with ideal conditions."
    ],
    "Interest": [
        "No interest (in sharing the data or code) is declared.",
        "No interest declared (but if this gets published, this may change).",
        "No interest in declaring interest is declared.",
        "No interest in following a reporting guideline is declared.",
        "No interest declared, but happy to cite this in ads for this app saying, \"Clinical research shows that...\".",
        "No interest declared, as we have no idea what \"conflict of interest\" even means.",
        "No interest declared, except for getting promoted or my thesis accepted with this study.",
        "No interest declared, but we'll gladly accept accolades if this gets a high impact factor."
    ]
}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate_paper():
    paper = (
        f"AI is poised to {random.choice(sections['Introduction'])}.\n"
        f"In this research, we test the use of {random.choice(sections['Methods'])} for the {random.choice(sections['For the'])}.\n"
        f"We trained a {random.choice(sections['Methods'])} in some data we found and validated, beyond any doubt, our results using {random.choice(sections['Validation'])}.\n"
        f"The dataset is {random.choice(sections['Dataset'])} and about the code {random.choice(sections['Code'])}.\n"
        f"Results: {random.choice(sections['Results'])}.\n"
        f"Discussion: {random.choice(sections['Discussion'])}.\n"
        f"Conflict of interest declaration: {random.choice(sections['Interest'])}."
    )
    return jsonify({"paper": paper})

if __name__ == '__main__':
    app.run(debug=True)
