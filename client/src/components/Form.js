import React from 'react';
import { useFormik } from 'formik';
import * as yup from 'yup';
import './Form.css'; // Ensure this file exists and is correctly styled

export const Form = ({ updateWorkoutClasses }) => {
  const formSchema = yup.object().shape({
    studio_name: yup.string().required("Studio name is required"),
    studio_location: yup.string().required("Studio location is required"),
    class_name: yup.string().required("Class name is required"),
    class_duration: yup.number().integer("Class duration must be an integer").required("Class duration is required"),
    class_date: yup.string().nullable(), // Allow null if not provided
    class_time: yup.string().nullable() // Allow null if not provided
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
      console.log(values.class_date)
      console.log(values.class_time)
      const formattedValues = {
        ...values,
        class_date: values.class_date ? new Date(values.class_date).toISOString() : "", // Use full ISO format
        class_time: values.class_time ? values.class_time : "", // Adjust format for time
      };
  
      console.log(formattedValues.class_date);
      console.log(formattedValues.class_time);
      

      fetch("http://localhost:5555/workoutclasses", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formattedValues),
      })

      .then((res) => {
        if (res.ok) { // Check for response status
          updateWorkoutClasses(); // Update the workout classes list
          formik.resetForm(); // Optionally reset the form
        } else {
          console.error("Error submitting form:", res.statusText);
        }
      })
      .catch((error) => {
        console.error("Error submitting form:", error);
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
            <p className="error-message">{formik.errors.studio_name}</p>
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
            <p className="error-message">{formik.errors.studio_location}</p>
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
            <p className="error-message">{formik.errors.class_name}</p>
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
            <p className="error-message">{formik.errors.class_duration}</p>
          ) : null}
        </div>

        <div className="form-group">
          <label htmlFor="class_date">Class Date</label>
          <input
            id="class_date"
            name="class_date"
            type="date"
            onChange={(e) => {
              formik.handleChange(e);
              console.log(e.target.value);
              }}
            value={formik.values.class_date}
          />
          {formik.errors.class_date ? (
            <p className="error-message">{formik.errors.class_date}</p>
          ) : null}
        </div>

        <div className="form-group">
          <label htmlFor="class_time">Class Time</label>
          <input
            id="class_time"
            name="class_time"
            type="time"
            onChange={(e) => {
            formik.handleChange(e);
            console.log(e.target.value);
            }}
          value={formik.values.class_time}
            />
          {formik.errors.class_time ? (
            <p className="error-message">{formik.errors.class_time}</p>
          ) : null}
        </div>

        <div className="form-group">
          <button className="button" type="submit">Submit Class</button>
        </div>
      </form>
    </div>
  );
};