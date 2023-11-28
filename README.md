
# OSROKBOT - Open Source Rise of Kingdoms Bot

OSROKBOT is a highly customizable, open-source bot for Rise of Kingdoms. Utilizing state machines and image detection, it provides a powerful platform for automation within the game. It is designed to be scalable, working with any 16:9 ratio screen.
This bot is not intended for comercial use. More than anything, this project should be a fun example for developers to play with.

## Actions

- **Scout Exploration:** Scouts explore fog and structures when available.
- **Farm Barbarians:** Farms barbarians at the pre-set level with lohar (you can change the commander) or all commanders in the field.
![Farming Barbarians](Media/Readme/farmbarbs.gif)

- **Farm Resources:** Farms resources at the automaticly chosen gatherers. For this, it is recommended that you use 720p res for now.
![Farming Resources](Media/Readme/farmrss.gif)
- **Catcha Recogniztion:** Will pause when captcha is detected and email you. You can then manually solve the captcha and the bot will continue.
- **Lyceum:** Will automatically do the lyceum event.
![Lyceum](Media/Readme/lyceum.gif)
- **Lyceum Midterm:** Will automatically do the lyceum midterm and finals event.
<img src="Media/Readme/lyceumwin1.png" width="800">
<img src="Media/Readme/lyceumwin2.png" width="800">



## Features

- **Highly Customizable:** Developers can implement new actions or create new state machines using the actions and images already provided.
- **Image Detection:** Uses sophisticated image detection techniques (it's literally just match template for now lol) to identify and respond to in-game events.
- **Screen Positioning:** Works seamlessly with various screen positions and resolutions.
- **Predefined Actions:** Comes with a set of predefined actions (find and click image, manual click position, press key, send email, chatgpt, extract text from image, etc), making it easy to extend or build new functionalities.
- **Predefined State Machines:** Machine use actions in states, states points to new state depending on success result of the action. (For now it's, lyceum, lyceum midterm, farm rss, farm barbs and detect captcha).

## Getting Started

### Prerequisites

- **Tesseract:** OSROKBOT requires Tesseract binaries. You must install them on your system.
- **Env:** Install Python
- **Python Libraries:** Install the required Python libraries by running (after running there may be errors related to other non installed libs, just install them for now):

  ```bash
  pip install -r requirements.txt
  ```

### Configuration

Create a `.env` file in the project root directory with the following content:

```env
OPENAI_KEY=your_openai_key
TESSERACT_PATH=your_tesseract_path
EMAIL=your_email
ANTIALIAS_METHOD=LANCZOS
```

Replace the placeholders with your actual values.

### Usage

You can create new state machines or actions using the existing framework. Feel free to screenshot your images for new state machines or different actions.
Remember to run the script as administrator.

## Development

Developers can extend OSROKBOT by implementing new actions or creating new state machines. The project provides a robust set of tools for working with images and actions.

## Support

If you need help or have any questions, please open an issue on the GitHub repository.

## License

OSROKBOT is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to the community and contributors (me) who have helped make OSROKBOT a reality.
