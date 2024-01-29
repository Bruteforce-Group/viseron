import Typography from "@mui/material/Typography";
import { useTheme } from "@mui/material/styles";
import { memo } from "react";

import { getTimeFromDate, timestampToDate } from "lib/helpers";

import { TICK_HEIGHT } from "./TimelineTable";

type TimeTickProps = {
  time: number;
};
export const TimeTick = memo(({ time }: TimeTickProps) => {
  const theme = useTheme();

  if (time % 300 === 0) {
    return (
      <div
        style={{
          display: "flex",
          justifyContent: "start",
          alignItems: "center",
          height: TICK_HEIGHT,
          minWidth: "58px",
          background: `linear-gradient(${theme.palette.divider}, ${theme.palette.divider}) no-repeat left/8px 1px`,
        }}
      >
        <Typography
          variant="body2"
          color="textSecondary"
          lineHeight={0}
          fontSize={9}
          style={{ marginLeft: "13px" }}
        >
          {getTimeFromDate(timestampToDate(time), false)}
        </Typography>
      </div>
    );
  }
  return (
    <div
      style={{
        height: TICK_HEIGHT,
        minWidth: "58px",
        background: `linear-gradient(${theme.palette.divider}, ${theme.palette.divider}) no-repeat left/4px 1px`,
      }}
    />
  );
});
