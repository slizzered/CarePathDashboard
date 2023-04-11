import Styles from "./Table.module.css";
import * as React from "react";
import Collapse from "@mui/material/Collapse";
import IconButton from "@mui/material/IconButton";
import KeyboardArrowDownIcon from "@mui/icons-material/KeyboardArrowDown";
import KeyboardArrowUpIcon from "@mui/icons-material/KeyboardArrowUp";

/*
 * Collapsible Table from @mui
 * https://mui.com/material-ui/react-table/#collapsible-table
 * Use of this source code is governed by an MIT-style license that can be found in the LICENSE file at https://mui.com/x/introduction/licensing/
 */

function createData(
  beginRT,
  treatment_task,
  patient,
  blocking_task,
  progress_overview
) {
  return {
    beginRT,
    treatment_task,
    patient,
    blocking_task,
    progress_overview,
  };
}

function Row(props) {
  const { row } = props;
  const [open, setOpen] = React.useState(false);

  return (
    <React.Fragment>
      <div className={Styles.table_row}>
        <div className={Styles.table_cell}>
          <IconButton
            aria-label="expand row"
            size="small"
            onClick={() => setOpen(!open)}
          >
            {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
          </IconButton>
        </div>
        <div className={Styles.table_cell_begin_rt}>{row.beginRT}</div>
        <div className={Styles.table_cell}>{row.treatment_task}</div>
        <div className={Styles.table_cell}>{row.patient}</div>
        <div className={Styles.table_cell}>{row.blocking_task}</div>
        <div className={Styles.table_cell}>{row.progress_overview}</div>
      </div>
      <Collapse in={open} timeout="auto" unmountOnExit>
        <h1>TestTest</h1>
      </Collapse>
    </React.Fragment>
  );
}

const rows = [
  createData(
    "2h",
    "erste RT Hyperarc",
    "Olaf",
    "OARs einzeichnen",
    "in Bearbeitung",
    4.0
  ),
  createData("5h", "erste RT", "Ralf", "PD vorbereiten", "Offen", 4.3),
  createData(
    "5h",
    "RT Boost",
    "Manuela",
    "PTV einzeichnen",
    "in Bearbeitung",
    6.0
  ),
  createData("10h", "erste RT", "Fritz", "Arzt Freigabe", "Verfügbar", 4.3),
  createData("12h", "erste RT", "Maike", "PTV anpassen", "in Bearbeitung", 3.9),
];

export default function CollapsibleTable() {
  return (
    <div className={Styles.table_container}>
      <div className={Styles.table_header}>
        <div className={Styles.table_cell}/>
        <div className={Styles.table_cell}/>
        <div className={Styles.table_cell}> Behandlungsbeginn </div>
        <div className={Styles.table_cell}>Patient(-ID)</div>
        <div className={Styles.table_cell}>Blocking Task</div>
        <div className={Styles.table_cell}>Progress Overview</div>
      </div>
      {rows.map((row) => (
        <Row key={row.beginRT} row={row} />
      ))}
    </div>
  );
}
