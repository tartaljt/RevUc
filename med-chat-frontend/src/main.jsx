import * as React from "react";
import * as ReactDOM from "react-dom/client";
import Root from "./routes/root";
import Journal from "./routes/journal";
import Providers from "./routes/providers";
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
          path: "providers/",
          element: <Providers />,
        },
        {
          path: "schedule/",
          element: <Schedule />,
        },
      ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);