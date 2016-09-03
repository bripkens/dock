function __all_dock_formulars
  dock -l | tail -n +2 | tr '\n' ' '
end

complete -c dock -a (__all_dock_formulars)
complete -c dock -s l -l list -d 'List available formulas'
complete -c dock -s c -l cat -a (__all_dock_formulars) -d 'Display formula details'
complete -c dock -s u -l upgrade -d 'Upgrade list of available formulas'
complete -c dock -s d -l rm -d 'Stop and remove all containers'
complete -c dock -s h -l help -d 'Display help text'
complete -c dock -s v -l version -d 'Display current script version'
