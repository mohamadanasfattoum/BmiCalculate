# BMI Calculator

This is a simple BMI (Body Mass Index) calculator built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python.

## Features

- Calculate BMI based on user's height and weight
- Provide BMI category and health risk information
- Responsive design for mobile and desktop

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mohamadanasfattoum/BmiCalculate.git
   ```

2. Navigate to the project directory:

   ```bash
   cd BmiCalculate
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI server:

   ```bash
   uvicorn BimCalc:app --reload
   ```

   This will start the server at `http://localhost:8000`.

2. Open your web browser and go to `http://localhost:8000`. You should see the BMI Calculator web page.

3. Enter your height (in centimeters) and weight (in kilograms), then click the "Calculate BMI" button.

4. The app will display your BMI, BMI category, and health risk information.

## API Endpoint

The BMI calculation is also exposed as a FastAPI endpoint:

- **Endpoint**: `POST /calculate_bmi`
- **Request Body**:
  ```json
  {
    "height": 1.7,
    "weight": 70
  }
  ```
- **Response**:
  ```json
  {
    "bmi": 24.22,
    "bmi_category": "Normal weight",
    "health_risk": "Low risk"
  }
  ```

You can test the API endpoint using tools like Postman or curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"height": 170, "weight": 70}' http://localhost:8000/calculate_bmi
```

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

To use the FastAPI project:

1. Start the FastAPI server by running the following command in the project directory:

   ```bash
   uvicorn BimCalc:app --reload
   ```

   This will start the server at `http://localhost:8000`.

2. Open your web browser and go to `http://localhost:8000`. You should see the BMI Calculator web page.

3. Enter your height (in meters) and weight (in kilograms), then click the "Calculate BMI" button.

4. The app will display your BMI, BMI category, and health risk information.

5. You can also use the API endpoint to calculate the BMI programmatically. Send a POST request to `http://localhost:8000/calculate_bmi` with a JSON payload containing the height and weight:

   ```json
   {
     "height": 1.7,
     "weight": 70
   }
   ```

   The response will contain the BMI, BMI category, and health risk information.

   ### project screenshot
![](https://github.com/mohamadanasfattoum/BmiCalculate/blob/main/screencapture.png)
