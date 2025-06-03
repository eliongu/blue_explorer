# Blue Explorer

## **GreenTunnel**

## Contexte

**GreenTunnel** est une PME spécialisée dans la **gestion des réseaux de ventilation et d’irrigation souterrains** pour les serres agricoles, les bâtiments industriels et les fermes verticales.

Ces installations possèdent des **galeries techniques étroites**, **peu éclairées** et parfois **inaccessibles à l’homme**.

Lors de leurs inspections, les techniciens doivent souvent ramper dans des conduits exigus ou démonter des sections entières pour accéder à certaines zones. Ce processus est lent, inconfortable, voire dangereux.

## Objectif

L’entreprise **GreenTunnel** nous a sollicité pour concevoir un outil d’exploration robotique simple, fiable et autonome afin d’améliorer ses interventions techniques dans les zones difficiles d’accès.
Notre objectif est de proposer une solution **efficace, mobile et économique**, combinant **contrôle manuel**, **navigation autonome**, **détection d’obstacles** et **affichage d’état clair**.


- **Sujet**
    - Robot mobile combinant un mode manuel pour les inspections ciblées et un mode autonome avec évitement d’obstacles, équipé d’un affichage LED pour signaler son état ou sa direction, adapté aux environnements techniques exigus.
    - Concevoir un **robot explorateur** capable de se déplacer dans un environnement inconnu, en pilotage **manuel** ou **autonome**.
- **Objectif**
    - Conception d’un **robot mobile basé sur une ESP32**
    - Implémentation d’un **mode manuel** et/ou d’un mode **autonome**
    - Contrôle via **joystick** ou **boutons**, utilisant **Bluetooth** ou **ESP-NOW**
    - Intégration possible de capteurs **infrarouge** ou **ultrasons**
    
- **Techno** :
    - Micropython
    
- **Livrable** :
    - [Schéma électronique Corps](schéma-elec-Corps.png)
    - [Schéma électronique Manette](schéma-elec-Manette.png)
    - Prototype complet (assemblage électronique et mécanique)
        - [Corps](Corps.jpg)
        - [Manette](Manette.jpg)
    - Protocole d’assemblage
        - fixation des moteurs à l'aide de vis et écrous M3
        - branchement sur l'esp32-C6 ref [Schéma électronique Corps](schéma-elec-Corps.png)
        - Branchement au pont en H ref [Description Pont en H (*L298N*)](Description_L298N.png)
    - [Bilan énergétique](Bilan_énergétique.xlsx)
    - Bills of materials (BOM)
    - Justification de choix de composants
    - Code source 
        - [Corps](télécommandé.py)
        - [Manette](pilotage.py)