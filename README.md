# Mira Presentation

## Visual Showcase

![Mira Background](assets/mira-bg.png)
![Dashboard Interface](assets/dashboard.png)
![Runthrough Demo](assets/runthrough-interface-.gif)

### Profile Analysis Examples (Static Images)
| Professional Analysis | Vulnerability Assessment |
|-----------------------|--------------------------|
| ![Alex Professional](assets/Alex-pro.png) | ![Alex Vulnerability](assets/Alex-vulnerability.png) |
| ![Diana Professional](assets/Diana-pro.png) | ![Diana Vulnerability](assets/Diana-vulnerability.png) |
| ![Kam Professional](assets/Kam-pro.png) | ![Kam Vulnerability](assets/Kam-vulnerability.png) |

### Profile Analysis Demos (Animated GIFs)

#### Kam's Analysis
| Professional Analysis | Vulnerability Assessment |
|-----------------------|--------------------------|
| ![Kam Professional GIF](assets/kalp.gif) | ![Kam Vulnerability GIF](assets/kalv.gif) |

#### Alex's Analysis  
| Professional Analysis | Vulnerability Assessment |
|-----------------------|--------------------------|
| ![Alex Professional GIF](assets/alexp.gif) | ![Alex Vulnerability GIF](assets/alexv.gif) |

#### Diana's Analysis
| Professional Analysis | Vulnerability Assessment |
|-----------------------|--------------------------|
| ![Diana Professional GIF](assets/dianap.gif) | ![Diana Vulnerability GIF](assets/dianav.gif) |


## Mirastral

![Profile Generation](assets/profile_gen.png)


```mermaid
graph TD
    D[Dispatcher] --> |Profiles| Q1[Redis Queue 1]
    D --> |Profiles| Q2[Redis Queue 2]
    D --> |Profiles| Q3[Redis Queue 3]
    Q1 --> W1[Worker 1]
    Q2 --> W2[Worker 2]
    Q3 --> W3[Worker 3]
    W1 --> |JSON Output| O1[Output Dir 1]
    W2 --> |JSON Output| O2[Output Dir 2]
    W3 --> |JSON Output| O3[Output Dir 3]
```

### Fine Tune

![MiraStral Demo](assets/mirastral.gif)

```mermaid
graph TD
    A[Input JSON Files] --> B[Data Preprocessing]
    B --> C[File Tracking]
    C --> D[Checkpoint Check]
    D --> |No Checkpoint| E[Initialize Training]
    D --> |Found Checkpoint| F[Resume Training]
    E --> G[Training Loop]
    F --> G
    G --> |Every 100 Steps| H[Save Checkpoint]
    G --> |51 Minutes| I[Graceful Stop]
    G --> |Interrupt Signal| I
    I --> J[Save Final State]
    H --> G
    J --> K[Output Model]
```