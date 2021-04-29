scriptInfo(DO NOT PUT IN YOUR SCRIPT){
  scriptType = Regular/ServerScript
  typeTime = ~1m-2m
  difficulty = Easy
  codeLanguage = RobloxStudio Lua
}

//[Before you start, do these steps:
1. Find some music in the toolbox, and put them in a folder
2. Name each of the music 1, 2, 3, 4, etc.
3. Name the folder Music
4. Put the folder in SoundService
5. Insert a regular script in it
6. Open the script
7. NOTE: We will be using an example with 1 song, if you have more than one, please refer to YouTube
8. Let's begin!
]

local Music1 = game.SoundService.Music.Music1

function PlayMusic()(
  Music1:Play()
end)

game.Players.PlayerAdded:Connect(PlayMusic())


if Music1.Ended then
  PlayMusic()
end
