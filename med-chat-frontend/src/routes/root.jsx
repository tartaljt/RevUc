import { Outlet } from "react-router-dom";

export default function Root() {
    return (
      <>
        <div id="sidebar">
          <h1>MCS</h1>
          <nav>
            <ul>
              <li>
                <a href={`/journal`}>Write in Journal</a>
              </li>
              <li>
                <a href={`/call`}>Video Call</a>
              </li>
              <li>
                <a href={`/schedule`}>Schedule</a>
              </li>
            </ul>
          </nav>
        </div>
        <div id="detail">
            <Outlet />
        </div>
      </>
    );
  }