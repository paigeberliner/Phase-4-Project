/*import React, { useEffect, useState } from "react";
import { useFormik } from "formik";
import * as yup from "yup";
import './Form.css'; // Assuming this is the CSS file for styling

export const Form = () => {
  const [workoutClasses, setWorkoutClasses] = useState([]);
  const [refreshPage, setRefreshPage] = useState(false);

  useEffect(() => {
    fetch("/workoutclasses")
      .then((res) => res.json())
      .then((data) => {
        setWorkoutClasses(data);
      });
  }, [refreshPage]);

  const formSchema = yup.object().shape({
    studio_name: yup.string().required("Studio name is required"),
    studio_location: yup.string().required("Studio location is required"),
    class_name: yup.string().required("Class name is required"),
    class_duration: yup
      .number()
      .integer("Class duration must be an integer")
      .required("Class duration is required"),
    class_date: yup.date().required("Class date is required"),
    class_time: yup
      .string()
      .matches(/^([0-1]\d|2[0-3]):([0-5]\d)$/, "Invalid time format")
      .required("Class time is required"),
  });

  const formik = useFormik({
    initialValues: {
      studio_name: "",
      studio_location: "",
      class_name: "",
      class_duration: "",
      class_date: "",
      class_time: "",
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch("/workoutclasses", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values, null, 2),
      }).then((res) => {
        if (res.status === 200) {
          setRefreshPage(!refreshPage);
        }
      });
    },
  });

  return (
    <div className="form-container">
      <h2>Submit a Workout Class</h2>
      <form onSubmit={formik.handleSubmit}>
        <div className="form-group">
          <label htmlFor="studio_name">Studio Name</label>
          <input
            id="studio_name"
            name="studio_name"
            type="text"
            onChange={formik.handleChange}
            value={formik.values.studio_name}
          />
          {formik.errors.studio_name ? (
            <p style={{ color: "red" }}>{formik.errors.studio_name}</p>
          ) : null}
        </div>

        <div className="form-group">
          <label htmlFor="studio_location">Studio Location</label>
          <input
            id="studio_location"
            name="studio_location"
            type="text"
            onChange={formik.handleChange}
            value={formik.values.studio_location}
          />
          {formik.errors.studio_location ? (
            <p style={{ color: "red" }}>{formik.errors.studio_location}</p>
          ) : null}
        </div>

        <div className="form-group">
          <label htmlFor="class_name">Class Name</label>
          <input
            id="class_name"
            name="class_name"
            type="text"
            onChange={formik.handleChange}
            value={formik.values.class_name}
          />
          {formik.errors.class_name ? (
            <p style={{ color: "red" }}>{formik.errors.class_name}</p>
          ) : null}
        </div>

        <div className="form-group">
          <label htmlFor="class_duration">Class Duration (minutes)</label>
          <input
            id="class_duration"
            name="class_duration"
            type="number"
            onChange={formik.handleChange}
            value={formik.values.class_duration}
          />
          {formik.errors.class_duration ? (
            <p style={{ color: "red" }}>{formik.errors.class_duration}</p>
          ) : null}
        </div>

        <div className="form-group">
          <label htmlFor="class_date">Class Date</label>
          <input
            id="class_date"
            name="class_date"
            type="date"
            onChange={formik.handleChange}
            value={formik.values.class_date}
          />
          {formik.errors.class_date ? (
            <p style={{ color: "red" }}>{formik.errors.class_date}</p>
          ) : null}
        </div>

        <div className="form-group">
          <label htmlFor="class_time">Class Time</label>
          <input
            id="class_time"
            name="class_time"
            type="time"
            onChange={formik.handleChange}
            value={formik.values.class_time}
          />
          {formik.errors.class_time ? (
            <p style={{ color: "red" }}>{formik.errors.class_time}</p>
          ) : null}
        </div>

        <div className="form-group">
          <button className="button" type="submit">
            Submit Class
          </button>
        </div>
      </form>
    </div>
  );
};*/
