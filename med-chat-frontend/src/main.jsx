import * as React from "react";
import * as ReactDOM from "react-dom/client";
import Root from "./routes/root";
import Journal from "./routes/journal";
import Call from "./routes/call";
import Schedule from "./routes/schedule";
import ErrorPage from "./error-page";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import "./index.css";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <ErrorPage />,
    children: [
        {
          path: "journal/",
          element: <Journal />,
        },
        {
          path: "call/",
          element: <Call />,
        },
        {
          path: "schedule/",
          element: <Schedule />,
        },
        //{
        //  path: "monitor/",
        //  element: <Monitor />,
        //},
      ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);