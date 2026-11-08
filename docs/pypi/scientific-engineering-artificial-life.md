# Scientific/Engineering / Artificial Life

[Index](README.md) · 1 packages in this topic, by downloads.

### textworld

Microsoft Textworld - A Text-based Learning Environment.

`pip install textworld` · installs (wheel) · licence: not stated · rank 14419 · last release 2026-01-30 · [PyPI](https://pypi.org/project/textworld/)

<details><summary>README extract</summary>

A text-based game generator and extensible sandbox learning environment for training and testing reinforcement learning (RL) agents. Also check out aka.ms/textworld for more info about TextWorld and its creators. Have questions or feedback about TextWorld? Send them to textworld@microsoft.com or use the Gitter channel listed above.

Example:
```python
import textworld.gym

# Register a text-based game as a new environment.
env_id = textworld.gym.register_game("tw_games/custom_game.z8",
                                     max_episode_steps=50)

env = textworld.gym.make(env_id)  # Start the environment.

obs, infos = env.reset()  # Start new episode.
env.render()

...
```

...

</details>

