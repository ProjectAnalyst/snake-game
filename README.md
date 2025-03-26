# Snake Game Sample Project

This is a sample project that demonstrates the initial implementation of a Snake game, along with a detailed whitepaper outlining planned enhancements. This project will be used to test the Project Evolver system's ability to translate whitepaper specifications into code changes.

## Project Structure

```
sample_project/
├── README.md           # This file
├── genesis_prompt.md   # Initial prompt for basic implementation
├── whitepaper.md       # Detailed enhancement specifications
├── requirements.txt    # Project dependencies
└── game.py            # Current game implementation
```

## Current Features

- Basic snake movement using arrow keys
- Food spawning and collection
- Score tracking
- Collision detection (walls and self)
- Simple graphics using Pygame

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python game.py
```

## Controls

- Arrow keys: Control snake direction
- Close window to exit

## Future Development

This project serves as a test case for the Project Evolver system. The `whitepaper.md` file contains detailed specifications for future enhancements, which will be implemented using the Project Evolver's automated code generation and modification capabilities.

## Testing Project Evolver

To test how Project Evolver processes this project:

1. Point Project Evolver to this directory
2. Provide the whitepaper.md as input
3. Let the system analyze and implement the planned enhancements

The system should:
1. Read and understand the whitepaper
2. Break down the enhancements into manageable tasks
3. Generate and modify code to implement features
4. Maintain code quality and test coverage
5. Track progress and state 