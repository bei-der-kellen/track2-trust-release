const options = [
  {
    id: 'azure',
    name: 'Azure Open AI',
    tooltip: "Hover info for Azure Open AI"
  },
  {
    id: 'albert',
    name: 'Albert',
    tooltip: "Albert est l'option la plus sécurisée, optimisée pour aider dans les tâches administratives."
  }
];

function OptionsSelector() {
  return (
    <div className="options-container">
      {options.map((option) => (
        <div key={option.id} className="option-card" title={option.tooltip}>
          {option.name}
        </div>
      ))}
    </div>
  );
}

export default OptionsSelector; 