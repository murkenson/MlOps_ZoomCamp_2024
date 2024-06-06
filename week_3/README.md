## Quickstart

1. Change directory into the cloned repo:

    ```bash
    git clone https://github.com/murkenson/MlOps_ZoomCamp_2024.git &&  cd /MlOps_ZoomCamp_2024/week_3
    ```

2. Launch Mage, the database service (PostgreSQL), pgAdimn and MLflow:

    ```bash
    ./scripts/start.sh
    ```

If don't have bash in your enviroment, modify the following command and run it:

    ```bash
    PROJECT_NAME=mlops \
        MAGE_CODE_PATH=/home/src \
        SMTP_EMAIL=$SMTP_EMAIL \
        SMTP_PASSWORD=$SMTP_PASSWORD \
        docker compose up
    ```
It is ok if you get this warning, you can ignore it  
     `The "PYTHONPATH" variable is not set. Defaulting to a blank string.`


## Run example pipeline

1. Open [`http://localhost:6789`](http://localhost:6789) in your browser.

1. In the top left corner of the screen next to the Mage logo and **`mlops`** project name,
   click the project selector dropdown and choose the **`unit_0_setup`** option.

1. Click on the pipeline named **`example_pipeline`**.
1. Click on the button labeled **`Run @once`**.
