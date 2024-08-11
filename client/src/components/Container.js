import React from "react";
import Class from "./Class";
import './Container.css';

function Container({ id, studio_name, class_name, studio_location, class_time, class_duration }) {
  return (
    <div className="class-grid">
      <Class
        key={id}
        studio_name={studio_name}
        class_name={class_name}
        studio_location={studio_location}
        class_time={class_time}
        class_duration={class_duration}
      />
    </div>
  );
}

export default Container;
