import { useEffect, useState } from "react";
import api from "./axiosConfig";
import { useNavigate } from "react-router-dom";

const Properties: React.FC = () => {
  const [properties, setProperties] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchProperties = async () => {
      try {
        const response = await api.get('/api/properties/');
        if (response.message === "Go to login now") {
          console.log("error is gotten here");
          setProperties([]);
          navigate('/login/');
        }
        else {
          setProperties(response.data.results);
        }
      } catch (error) {
        console.error('Error fetching properties', error);
      }
    };

    fetchProperties();
  }, [navigate])

  return (
    <div>
      <h2>Property List</h2>
      <ul>
        {properties.map((property) => (
          <li key={property?.id}>{property?.name}</li>
        ))}
      </ul>
    </div>
  );
};


export default Properties;
