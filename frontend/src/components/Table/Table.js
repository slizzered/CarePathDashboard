import Styles from "./Table.module.css";
import * as React from "react";
import PropTypes from "prop-types";
import Box from "@mui/material/Box";
import Collapse from "@mui/material/Collapse";
import IconButton from "@mui/material/IconButton";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import KeyboardArrowDownIcon from "@mui/icons-material/KeyboardArrowDown";
import KeyboardArrowUpIcon from "@mui/icons-material/KeyboardArrowUp";

/*
 * Collapsible Table from @mui
 * https://mui.com/material-ui/react-table/#collapsible-table
 * Use of this source code is governed by an MIT-style license that can be found in the LICENSE file at https://mui.com/x/introduction/licensing/
 */

function createData(beginRT, patient, blocking_task, progress_overview) {
  return {
    beginRT,
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
      <tr className={Styles.table_row}>
        <td className={Styles.table_cell}>
          <IconButton
            aria-label="expand row"
            size="small"
            onClick={() => setOpen(!open)}
          >
            {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
          </IconButton>
        </td>
        <td className={Styles.table_cell} component="th" scope="row">
          {row.beginRT}
        </td>
        <td className={Styles.table_cell} align="right">
          {row.patient}
        </td>
        <td className={Styles.table_cell} align="right">
          {row.blocking_task}
        </td>
        <td className={Styles.table_cell} align="right">
          {row.progress_overview}
        </td>
      </tr>
      <tr>
        <td style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
          <Collapse in={open} timeout="auto" unmountOnExit>
            <h1>TestTest</h1>
          </Collapse>
        </td>
      </tr>
    </React.Fragment>
  );
}

Row.propTypes = {
  row: PropTypes.shape({
    calories: PropTypes.number.isRequired,
    carbs: PropTypes.number.isRequired,
    fat: PropTypes.number.isRequired,
    history: PropTypes.arrayOf(
      PropTypes.shape({
        amount: PropTypes.number.isRequired,
        customerId: PropTypes.string.isRequired,
        date: PropTypes.string.isRequired,
      })
    ).isRequired,
    beginRT: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
  }).isRequired,
};

const rows = [
  createData(
    "2h erste RT Hyperarc",
    "Olaf",
    "OARs einzeichnen",
    "in Bearbeitung",
    4.0
  ),
  createData("5h erste RT", "Ralf", "PD vorbereiten", "Offen", 4.3),
  createData(
    "5h RT Boost",
    "Manuela",
    "PTV einzeichnen",
    "in Bearbeitung",
    6.0
  ),
  createData("10h erste RT", "Fritz", "Arzt Freigabe", "Verfügbar", 4.3),
  createData("12h erste RT", "Maike", "PTV anpassen", "in Bearbeitung", 3.9),
];

export default function CollapsibleTable() {
  return (
    <TableContainer component="div">
      <Table aria-label="collapsible table">
        <thead className={Styles.table_header}>
          <tr className={Styles.table_row}>
            <th />
            <th className={Styles.table_cell}> Behandlungsbeginn </th>
            <th className={Styles.table_cell} align="right">
              Patient(-ID)
            </th>
            <th className={Styles.table_cell} align="right">
              Blocking Task
            </th>
            <th className={Styles.table_cell} align="right">
              Progress Overview
            </th>
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => (
            <Row key={row.beginRT} row={row} />
          ))}
        </tbody>
      </Table>
    </TableContainer>
  );
}
