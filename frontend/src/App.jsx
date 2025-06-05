import React, { useState, useCallback } from 'react';
import './App.css';

function App() {
  const [age, setAge] = useState(0.5);
  const [wealth, setWealth] = useState(0.5);
  const [probApple, setProbApple] = useState(0.5);
  const [probAndroid, setProbAndroid] = useState(0.5);
  const [predictedPhone, setPredictedPhone] = useState('Enter values to get a recommendation');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchPrediction = useCallback(async () => {
    setLoading(true);
    setError(null);

    const ageValue = parseFloat(age); 
    const wealthValue = parseFloat(wealth);

    if (isNaN(ageValue) || ageValue < 0 || ageValue > 1 || isNaN(wealthValue) || wealthValue < 0 || wealthValue > 1) {
      setError('Please enter numbers between 0 and 1 for Age and Wealth.');
      setPredictedPhone('Invalid input');
      setLoading(false);
      return;
    }

    const apiUrl = `http://localhost:5000/predict?age=${ageValue}&wealth=${wealthValue}`;

    try {
      const response = await fetch(apiUrl);

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log("API Response Data:", data);

      setPredictedPhone(data.predicted_phone || 'Could not get prediction');
      setProbAndroid(data.prob_android)
      setProbApple(data.prob_apple)

    } catch (e) {
      console.error("Failed to fetch prediction:", e);
      setError('Failed to fetch prediction. Make sure the API is running.');
      setPredictedPhone('Error fetching recommendation');
    } finally {
      setLoading(false);
    }
  }, [age, wealth]);

  const handlePredict = () => {
    fetchPrediction();
  };

  return (
    <div className="App min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-sm">
        <h1 className="text-2xl font-bold mb-6 text-center text-gray-800">Handy Vorhersage</h1>

        <div className="mb-4">
          <label htmlFor="age" className="block text-gray-700 text-sm font-bold mb-2">
            Wahrscheinlichkeit jung zu sein (0-1):
          </label>
          <input
            id="age"
            type="number"
            step="0.01"
            min="0"
            max="1"
            value={age}
            onChange={(e) => setAge(e.target.value)}
            className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="z.B. 0.8"
          />
        </div>

        <div className="mb-6">
          <label htmlFor="wealth" className="block text-gray-700 text-sm font-bold mb-2">
            Wahrscheinlichkeit reich zu sein (0-1):
          </label>
          <input
            id="wealth"
            type="number"
            step="0.01"
            min="0"
            max="1"
            value={wealth}
            onChange={(e) => setWealth(e.target.value)}
            className="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="z.B. 0.2"
          />
        </div>

        <div className="text-center mb-6">
          <button
            onClick={handlePredict}
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition duration-150 ease-in-out"
            disabled={loading}
          >
            {loading ? 'Vorhersage läuft...' : 'Vorhersagen'}
          </button>
        </div>

        <div className="mt-6 text-center">
          <h2 className="text-xl font-semibold text-gray-800">Handy: </h2>
          {loading && <p className="text-gray-500">Lädt...</p>}
          {error && <p className="text-red-500">{error}</p>}
          {!loading && !error && (
            <p className="text-green-600 text-lg font-bold mt-2">{predictedPhone}</p>
          )}
        </div>
        <div className="mt-4 text-center">
          <h3 className="text-md font-semibold text-gray-700 mb-2">Wahrscheinlichkeiten:</h3>
          <div className="flex flex-col gap-1">
            <span className="text-gray-800">
              <strong>Apple:</strong> {(probApple * 100).toFixed(1)}%
            </span>
            <span className="text-gray-800">
              <strong>Android:</strong> {(probAndroid * 100).toFixed(1)}%
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;