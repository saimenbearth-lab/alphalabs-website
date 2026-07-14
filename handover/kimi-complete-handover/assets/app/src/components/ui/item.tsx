import * as React from "react"
import { cn } from "@/lib/utils"

interface ItemProps extends React.HTMLAttributes<HTMLDivElement> {
  title: string
  description?: string
  icon?: React.ReactNode
  action?: React.ReactNode
  active?: boolean
}

const Item = React.forwardRef<HTMLDivElement, ItemProps>(
  ({ className, title, description, icon, action, active, children, ...props }, ref) => {
    return (
      <div
        ref={ref}
        className={cn(
          "flex items-center gap-3 rounded-lg border p-3 transition-colors",
          active && "border-primary bg-primary/5",
          !active && "hover:bg-muted/50",
          className
        )}
        {...props}
      >
        {icon && (
          <div className={cn(
            "flex h-10 w-10 shrink-0 items-center justify-center rounded-md",
            active ? "bg-primary/10 text-primary" : "bg-muted text-muted-foreground"
          )}>
            {icon}
          </div>
        )}
        <div className="flex-1 min-w-0">
          <p className="text-sm font-medium truncate">{title}</p>
          {description && (
            <p className="text-xs text-muted-foreground truncate">{description}</p>
          )}
          {children}
        </div>
        {action && <div className="shrink-0">{action}</div>}
      </div>
    )
  }
)
Item.displayName = "Item"

export { Item }
