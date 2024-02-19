# Actor Informator Infrastructure
Actor Informator Insfrastructure is a platform built to deploy a Macro-Based Action System and a Machine-Learning-Based Control System on a network. The primary use case is to automate old MMORPG games on old personal computers or more generally hardware-constrained systems (Node) using a centralized manager (Orchestrator). Actor and Informator are the two element who operate inside a node while Controller and Processor operate inside the Orchestrator.

## Actor - Controller
In this initial stage the Actor is a Macro-Based element, this means that it can send only keystrokes to the instances without taking into considerations the state of the instance. Its built using [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) and can be manged by the Controller who can send commands to modify the behavior of the Actor.

## Informator - Processor
The primary objective of the Informator is to capture important data about the instances and send them to the Processor, who can then aggregate and show them using a Dashboard.

# Base Progression
- [ ] Actor
  - [ ] Actor Server
  - [X] Actor Actions
- [ ] Deployment
  - [ ] Setup Script
  - [ ] Startup Script
- [ ] Informator
  - [ ] Train ML Model
  - [ ] Model Inference
- [ ] Controller
  - [ ] Commands
- [ ] Processor
  - [ ] Dashboard
     
