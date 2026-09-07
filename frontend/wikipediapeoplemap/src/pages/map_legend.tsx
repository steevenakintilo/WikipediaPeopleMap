import { useEffect } from "react";
import { useMap } from "react-leaflet";
import L from "leaflet";

const Legend = () => {
  const map = useMap();

  useEffect(() => {
    const legend = new L.Control({ position: "bottomleft" });
    
    legend.onAdd = () => {
      const div = L.DomUtil.create("div", "info legend");

      div.innerHTML = `
        <h4>Légende</h4>

        <div>
          <span class="legend-circle legend-birth-man-alive"></span>
          Lieu de naissance: Homme vivant
        </div>

        <div>
          <span class="legend-circle legend-birth-man-dead"></span>
          Lieu de naissance: Homme mort  
        </div>

        <div>
          <span class="legend-circle legend-death-man-place"></span>
          Lieu de mort: Homme mort  
        </div>
        
        <div>
          <span class="legend-circle legend-birth-woman-alive"></span>
            Lieu de naissance: Femme vivante
          </div>

        <div>
          <span class="legend-circle legend-birth-woman-dead"></span>
          Lieu de naissance: Femme morte
        </div>
        
        <div>
          <span class="legend-circle legend-death-woman-place"></span>
          Lieu de mort: Femme morte
        </div>
        
      `;

      return div;
    };

    legend.addTo(map);

    return () => {
      legend.remove();
    };
  }, [map]);

  return null;
};

export default Legend;

