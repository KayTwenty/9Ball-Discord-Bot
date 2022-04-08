<p align="center">
  <a href="https://sites.google.com/view/jesterbot">
    <img src="9ball.png" alt="Logo" width="150" height="150">
  </a>
  
  <h1 align="center">9Ball</h1>
  <p align="center">
  <img src="https://img.shields.io/github/last-commit/KayTwenty/9Ball-Discord-Bot?style=for-the-badge" alt="Commit"/>
  <img src="https://img.shields.io/github/license/KayTwenty/9Ball-Discord-Bot?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/badge/python-3.7+-blue?style=for-the-badge" alt="Python"/>
  <img src="https://img.shields.io/badge/code%20style-black-black?style=for-the-badge" alt="Black" />
  </p>
  <p align="center">
    A powerful eight ball and multipurpose discord bot!
    <br />
    <a href="">Explore Website</a>
    ·
    <a href="">Invite 9Ball</a>
  </p>
</p>

___
And yet again I haven't finished the rest for the markdown, this project is still maintained
___

## ⚙ Self-Hosting (LINUX ONLY)
**This guide is mainly written for Ubuntu/Debian**
- To start off make sure you have the base requirements: **Python3.7+, PIP, and Git**
- Create a discord bot application on [discord developer portal](https://discord.com/developers/applications), you can use [this guide](https://discordpy.readthedocs.io/en/latest/discord.html)

### Basic Setup
* Clone the repository\
`git clone https://github.com/KayTwenty/9Ball-Discord-Bot`
- CD your way into the projects root directory\
`cd path/to/9Ball`
- Setup your Virtual Environment (Venv)

```shell
python3 -m pip install venv #install venv
python3 -m venv venv #initialize the venv for this project
source venv/bin/activate #activate it
```

* After that you are set to now install the bot's requirements\
`pip` OR `pip3 install -r requirements.txt`
- Now once installed, you may start the bot using: `python3 main.py`
- Congrats you have the bot running 🎉

### Pm2 Setup
- Make sure you have the one of these: **npm or yarn**
- Install PM2 if you don't already have it\
`npm install pm2 -g` or `yarn global add pm2`
- After installing PM2 you are ready to run the bot\
`pm2 start pm2.json`

___

## License
This project is licensed under MIT - See the [LICENSE](LICENSE) file for details
