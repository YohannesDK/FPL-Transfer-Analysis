import React, { useEffect, useState } from "react";

interface BackendData {
    data: number[];
}

const App: React.FC = () => {
    const [data, setData] = useState<BackendData | null>(null);


    const backendUrl = import.meta.env.VITE_BACKEND_URL;


    useEffect(() => {
        fetch(`${backendUrl}/api/data`)
            .then((response) => response.json())
            .then((json) => setData(json))
            .catch((err) => console.error("Error fetching data:", err));
    }, []);


    return (
        <div>
            <h1>Frontend with Backend Integration</h1>
            <p>Backend Data:</p>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    );
};

export default App;

