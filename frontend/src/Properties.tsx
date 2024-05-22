import { useEffect, useState } from "react";
import api from "./axiosConfig";

const Properties: React.FC = () => {
  const [properties, setProperties] = useState([])

  useEffect(() => {
    const fetchProperties = async () => {
      try {
        const response = await api.get('/api/properties');
        setProperties(response.data);
      } catch (error) {
        console.error('Error fetching properties', error);
      }
    };

    fetchProperties();
  }, [])

  return (
    <div>
      <h2>Property List</h2>
      <ul>
        {properties.map((property) => {
          <li key={property.id}>{property.name}</li>
        })}
      </ul>
    </div>
  );
};


export default Properties;
