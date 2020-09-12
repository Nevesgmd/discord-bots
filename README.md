# Discord Bots Repository

A repository to store all the Discord bots that I create whenever me and my friends need a specific functionality

# Summary
1. [Commits Pattern](#commits)
2. [I have no experience with Discord bots](#no-experience)
3. [Running](#running)
4. [License](#license)


<a name="commits"></a>
## Commits Pattern
Feel free to contribute to the project with new bot ideas or code improvements!   
Just be sure to follow the commits pattern, explained [here](https://udacity.github.io/git-styleguide/).  

<a name="no-experience"></a>
## I have no experience with Discord bots
If you don't have any experience with Discord Bots I highly recommend you to watch some Youtube tutorials or search a little about the topic.  
I personally watched the first videos of this [Youtube tutorial](https://www.youtube.com/watch?v=nW8c7vT6Hl4&ab_channel=Lucas) from Lucas and it helped me a lot.  

<a name="running"></a>
## Running
This project was dockerized in order to make the running process easier, be sure that you have [Docker](https://www.docker.com/) installed before you follow the next steps. Also, it's necessary to create a bot in the [Discord Developers Website](https://discord.com/developers/) so that you can receive a token and run the bot in your discord server (read the **"I have no experience with Discord bots"** section if you never done this before).  
  
After performing the defined procedures above and downloading/clonning all the files present in this repository, follow these steps:

1. Access the project directory using the `terminal` (MacOS, Linux) or the `cmd` (Windows).
2. Be sure that you have a *.globalresources.json* file with the discord API token in the main directory.
2. Run the bot using docker-compose with the following command: `docker-compose up --build`

<a name="license"></a>
## License
This project is licensed under the GNU GPL v3.0 License - see the [LICENSE](LICENSE) file for details.
